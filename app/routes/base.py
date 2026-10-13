from fastapi import APIRouter

from app.routes import (
    ai_query,
    create_student,
    delete_students,
    get_students,
    update_students,
)

api_router = APIRouter()

api_router.include_router(ai_query.router)
api_router.include_router(create_student.router)
api_router.include_router(get_students.router)
api_router.include_router(update_students.router)
api_router.include_router(delete_students.router)

