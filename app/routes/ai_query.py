import re

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student

router = APIRouter(prefix="/ai", tags=["AI Query"])


class QueryRequest(BaseModel):
    question: str = Field(min_length=2, max_length=500)


@router.post("/query-students")
def ask_student_database(payload: QueryRequest, db: Session = Depends(get_db)):
    question = payload.question.strip()
    students = db.query(Student).order_by(Student.id).all()

    if re.search(r"\\b(how many|count|number of)\\b", question, re.IGNORECASE) and re.search(
        r"\\bstudents?\\b", question, re.IGNORECASE
    ):
        count = len(students)
        return {
            "question": question,
            "answer": f"There are {count} student{'s' if count != 1 else ''} in the database.",
            "source": "database",
        }

    # Use only fields that exist in the current Student model.
    context_data = "\\n".join(
        f"ID: {s.id}; Name: {s.student_name}; Course: {s.student_course}; "
        f"Section: {s.student_section}; DOB: {s.student_dob}; "
        f"Address: {s.student_address or 'Not provided'}"
        for s in students
    ) or "No student records are currently stored."

    prompt = f"""You are an assistant for a student database.
Answer using only the database context below. Do not invent details.
Do not reveal contact information unless explicitly requested.

Database context:
{context_data}

User question: {question}

Answer:"""

    try:
        from langchain_ollama import ChatOllama
        response = ChatOllama(model="llama3.2:1b", temperature=0).invoke(prompt)
        answer = response.content if hasattr(response, "content") else str(response)
        return {"question": question, "answer": answer, "source": "database_context"}
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Could not connect to Ollama. Ensure Ollama is running and `llama3.2:1b` is installed. "
                   f"Technical detail: {exc}",
        ) from exc
