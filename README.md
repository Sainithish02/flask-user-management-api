# Flask User Management REST API

This project is a backend REST API built using Flask and SQLite that supports full CRUD operations for managing users.

## Features
- Create users (POST /users)
- Retrieve all users (GET /users)
- Retrieve a specific user (GET /users/<id>)
- Update user details (PUT /users/<id>)
- Delete a user (DELETE /users/<id>)

## Tech Stack
- Python
- Flask
- SQLite
- REST API
- JSON

## Project Structure
app.py – Main application entry point  
database.py – Database connection handling  
models/ – Database query logic  
routes/ – API route definitions  

## Example API Request

Create user:

POST /users