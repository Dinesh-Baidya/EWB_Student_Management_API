
from datetime import date
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)


class StudentBase(BaseModel):
    student_name: str = Field(min_length=1, max_length=120)
    student_dob: date
    student_address: Optional[str] = Field(default=None, max_length=120)
    student_course: str = Field(min_length=1, max_length=80)
    student_section: str = Field(min_length=1, max_length=40)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=7, max_length=30)

    @field_validator(
        "student_name",
        "student_course",
        "student_section",
        "student_address",
        mode="before",
    )
    @classmethod
    def strip_text(cls, value):
        if isinstance(value, str):
            value = value.strip()
            return value or None if value == "" else value
        return value

    @field_validator("phone", mode="before")
    @classmethod
    def normalize_phone(cls, value):
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value

    @model_validator(mode="after")
    def require_contact(self):
        if not self.email and not self.phone:
            raise ValueError("Provide at least one contact field: email or phone.")
        return self


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    student_name: Optional[str] = Field(default=None, min_length=1, max_length=120)
    student_dob: Optional[date] = None
    student_address: Optional[str] = Field(default=None, max_length=120)
    student_course: Optional[str] = Field(default=None, min_length=1, max_length=80)
    student_section: Optional[str] = Field(default=None, min_length=1, max_length=40)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(default=None, min_length=7, max_length=30)

    @field_validator(
        "student_name",
        "student_course",
        "student_section",
        "student_address",
        mode="before",
    )
    @classmethod
    def strip_optional_text(cls, value):
        if isinstance(value, str):
            value = value.strip()
        return value

    @field_validator("phone", mode="before")
    @classmethod
    def normalize_phone(cls, value):
        if isinstance(value, str):
            value = value.strip()
            return value or None
        return value


class StudentResponse(BaseModel):
    id: int
    student_name: str
    student_dob: date
    student_address: Optional[str] = None
    student_course: str
    student_section: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)
