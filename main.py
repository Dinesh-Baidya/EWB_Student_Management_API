from fastapi import FastAPI

from app.database import Base, engine, migrate_student_contact_columns
from app.routes.base import api_router
from app import model  # Ensure SQLAlchemy models are registered with Base.metadata

Base.metadata.create_all(bind=engine)
migrate_student_contact_columns()

app = FastAPI(
    title="Student Management API",
    description="Student CRUD API using FastAPI, SQLite, SQLAlchemy, and optional local Ollama AI",
    version="1.1.0",
)

app.include_router(api_router)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Welcome to Student Management API. Visit /docs for Swagger UI."
    }
