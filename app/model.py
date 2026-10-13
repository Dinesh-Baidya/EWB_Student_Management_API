from sqlalchemy import Column, Date, Integer, String
from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_name = Column(String(120), index=True, nullable=False)
    student_dob = Column(Date, nullable=False)
    student_address = Column(String(120), nullable=True)
    student_course= Column(String(80), nullable=False)
    student_section = Column(String(40), nullable=False)
    email = Column(String(254), nullable=True, unique=True, index=True)
    phone = Column(String(30), nullable=True)
