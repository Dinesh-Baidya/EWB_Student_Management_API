from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = settings.database_url

connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def migrate_student_contact_columns():
    """Safely add columns expected by the current model to an older SQLite table."""
    if not SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
        return

    with engine.begin() as connection:
        exists = connection.exec_driver_sql(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='students'"
        ).first()
        if not exists:
            return

        columns = {
            row[1] for row in connection.exec_driver_sql("PRAGMA table_info(students)").fetchall()
        }

        # Defaults let existing rows remain readable after adding required model fields.
        additions = {
            "student_address": "VARCHAR(120)",
            "student_course": "VARCHAR(80) NOT NULL DEFAULT ''",
            "student_section": "VARCHAR(40) NOT NULL DEFAULT ''",
            "email": "VARCHAR(254)",
            "phone": "VARCHAR(30)",
        }
        for column, sql_type in additions.items():
            if column not in columns:
                connection.exec_driver_sql(f"ALTER TABLE students ADD COLUMN {column} {sql_type}")

        # Copy old field values forward when migrating an older version of this project.
        if "student_class" in columns:
            connection.exec_driver_sql(
                "UPDATE students SET student_course = student_class "
                "WHERE (student_course IS NULL OR student_course = '') AND student_class IS NOT NULL"
            )
        if "student_sub" in columns:
            connection.exec_driver_sql(
                "UPDATE students SET student_section = student_sub "
                "WHERE (student_section IS NULL OR student_section = '') AND student_sub IS NOT NULL"
            )
