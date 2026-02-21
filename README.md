# Task Manager API
REST API built with FastAPI for managing tasks.
This project demonstrates CRUD operations, layered architecture, and database integration using SQLAlchemy.

## Features
- Create tasks
- List all tasks
- Update existing tasks
- Delete tasks
- Data validation with Pydantic
- Layered architecture (routers, models, schemas, CRUD)

## Technologies
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Git

## Project Structure
app/
├── main.py        # Application entry point
├── models.py      # Database models
├── schemas.py     # Pydantic schemas
├── crud.py        # Database operations
├── database.py    # Database configuration

## Instalación
git clone https://github.com/mariomirandadev/task-manager-api.git
cd task-manager-api
pip install -r requirements.txt

## Run the project
```bash
uvicorn app.main:app --reload
```

Then open your browser at:
http://127.0.0.1:8000/docs

## Future Improvements
- Implement authentication and user management
-  Add pagination to task listing
- Include automated testing
- Dockerize the application
- Deploy to a cloud platform