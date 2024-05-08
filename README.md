# ToDo List App using Python FastAPI

This is a simple ToDo List application built using Python's FastAPI framework. The application provides a RESTful API for managing a list of todo items.

## Project Structure

The project is structured into several Python files:

- `database.py`: This file sets up the database engine, base class for the models, and session factory for the database operations using MONGODB.
- `models.py`: This file defines the `TodoCreate` and `TodoUpdate` model which represents a todo item in the database.
- `authentication.py`: verifies user credentials and retrieves the current user, ensuring access control for protected routes.
- `main.py`: This file contains the FastAPI application and all the API endpoints.

## API Endpoints

The application provides the following API endpoints:

- `GET /todos`: Returns a welcome message.
- `POST /todos`: Creates a new todo item.
- `GET /todos/{id}`: Returns a todo item by its id.
- `PUT /todos/{id}`: Updates a todo item by its id.
- `DELETE /todos/{id}`: Deletes a todo item by its id.


## Setup and Run

To set up and run the application, follow these steps:

1. Install the required Python packages using:
```bash
pip install -r requirements.txt
```
2. cd app/

3. Run the main.py file using :
```bash
uvicorn main:app --reload
```