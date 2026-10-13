from datetime import date
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student
from app.schemas import StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[StudentResponse])
def get_all_students(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    name: Optional[str] = Query(default=None, description="Filter by part of a student's name"),
    student_course: Optional[str] = Query(default=None, description="Filter by course"),
    section: Optional[str] = Query(default=None, description="Filter by section"),
    born_after: Optional[date] = Query(default=None, description="Return students born after this date"),
    db: Session = Depends(get_db),
):
    query = db.query(Student)
    if name and name.strip():
        query = query.filter(Student.student_name.ilike(f"%{name.strip()}%"))
    if student_course and student_course.strip():
        query = query.filter(Student.student_course.ilike(f"%{student_course.strip()}%"))
    if section and section.strip():
        query = query.filter(Student.student_section.ilike(f"%{section.strip()}%"))
    if born_after:
        query = query.filter(Student.student_dob > born_after)
    return query.order_by(Student.id).offset(skip).limit(limit).all()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student
