from flask import Flask,request,jsonify
import sqlite3
app = Flask(__name__)
def init_db():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE  IF not exists users(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       USERNAME TEXT NOT NULL,
                       EMAIL TEXT NOT NULL)
                       """)
    conn.commit()
    conn.close()
init_db()
@app.route("/users", methods = ["GET"])
def users():
    conn=sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users= cursor.fetchall()
    conn.close()
    result = []
    for row in users:
        result.append({
            "id":row[0],
            "username":row[1],
            "email":row[2]

        })
    return jsonify(result)
@app.route("/users", methods = ["POST"])
def create_users():
    username = request.json.get("username")
    email = request.json.get("email")
    if not username or not email:
        return jsonify({"error":"invalid input"}),400
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("insert INTO users(username,email)VALUES(?,?)",
                   (username,email))

    conn.commit()
    conn.close()
    return jsonify({"success":"user created"}),201

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()

    conn.close()

    if row is None:
        return jsonify({"error": "User not found"}), 404

    user = {
        "id": row[0],
        "username": row[1],
        "email": row[2]
    }

    return jsonify(user), 200

if __name__ == "__main__":
    app.run(debug=True,port=5001)