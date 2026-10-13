# Student Management API — EWB Edu Tech Internship Project

A RESTful Student Management API built using **Python, FastAPI, SQLAlchemy, and SQLite** as part of the EWB Edu Tech Pvt. Ltd. Python Backend Development Internship Project.

The application provides complete CRUD (Create, Read, Update, Delete) operations for student records, input validation, persistent database storage, and an optional local AI extension using Ollama.

## Table of Contents

- [Project Overview](#project-overview)
- [Assignment Requirements](#assignment-requirements)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Environment Configuration](#environment-configuration)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Sample API Requests](#sample-api-requests)
- [Database Design](#database-design)
- [Optional AI Integration with Ollama](#optional-ai-integration-with-ollama)
- [Testing the API](#testing-the-api)
- [Error Handling](#error-handling)
- [Security Considerations](#security-considerations)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

## Project Overview

The Student Management API is a backend application designed to manage student information through RESTful HTTP endpoints.

It uses FastAPI to expose API routes and SQLite to store student records persistently. SQLAlchemy is used for database operations, while Pydantic schemas validate incoming request data and structure API responses.

The application supports creating new student records, listing and filtering students, retrieving individual student profiles, updating existing records, and deleting records.

An optional Ollama integration allows users to ask natural-language questions about student data stored in the database.

## Assignment Requirements

This project is designed to address the requirements of the EWB Edu Tech Python Backend Development Internship Assignment.

| Requirement | Implementation |
|---|---|
| Create student records | `POST /students/` |
| List and filter students | `GET /students/` |
| Retrieve a student by ID | `GET /students/{student_id}` |
| Update student details | `PUT /students/{student_id}` |
| Delete student records | `DELETE /students/{student_id}` |
| Required technology | Python, FastAPI, SQLite |
| Student data validation | Pydantic schemas |
| Persistent storage | SQLite database |
| Missing-record handling | HTTP 404 responses |
| API documentation | Swagger UI and ReDoc |
| Optional AI extension | Ollama-based natural-language queries |

The core CRUD application is the mandatory part of the assignment. The Ollama AI extension is optional.

## Features

- **Create:** Add new student records with validated information.
- **Read:** Retrieve all students or an individual student by ID.
- **Filter:** Search student records using supported query parameters.
- **Update:** Modify an existing student's information.
- **Delete:** Remove a student record from the database.
- **Persistent storage:** Store records in an SQLite database.
- **Input validation:** Validate incoming data using Pydantic.
- **Error handling:** Return appropriate HTTP status codes for invalid requests and missing records.
- **Interactive documentation:** Explore and test endpoints using Swagger UI.
- **Optional AI queries:** Ask natural-language questions about stored student records using a locally running Ollama model.

## Technology Stack

- **Python** — Backend programming language.
- **FastAPI** — REST API framework.
- **Uvicorn** — ASGI server.
- **SQLite** — Relational database.
- **SQLAlchemy** — ORM for database operations.
- **Pydantic** — Request validation and response schemas.
- **Ollama** — Optional local language-model integration.

## Project Structure

The main application files are organized as follows. Adjust filenames below if your repository uses different names.

```text
EWB_Student_Management_API/
│
├── app/
│   ├── routes/
│   │   ├── create_students.py
│   │   ├── get_students.py
│   │   ├── update_students.py
│   │   ├── delete_students.py
│   │   └── ai_query.py
│   │
│   ├── database.py
│   ├── model.py
│   └── schemas.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

The SQLite database file, such as `students.db`, may be created when the application starts. The exact location depends on the configured database URL.

## Prerequisites

Install the following before running the project:

- Python 3.10 or a compatible version supported by the dependencies.
- pip, Python's package installer.
- Git, if cloning the repository.
- A terminal such as Windows PowerShell, Command Prompt, or a Linux/macOS terminal.

Ollama is required only if you want to use the optional AI features.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Dinesh-Baidya/EWB_Student_Management_API.git
cd EWB_Student_Management_API
```

### 2. Create a virtual environment

On Windows:

```powershell
py -3.11 -m venv venv
```

Activate it in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run this command in the current terminal and activate the environment again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

On Linux or macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

If the repository contains `requirements.txt`:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If the dependency file has not been created, install the core dependencies:

```bash
python -m pip install fastapi "uvicorn[standard]" sqlalchemy pydantic-settings python-dotenv
```

Install any additional packages required by the optional AI module, such as `langchain-ollama`, if used by the implementation.

**Important:** Keep the dependency file in the repository up to date. After installing the required packages, you can generate one using:

```bash
python -m pip freeze > requirements.txt
```

Review the generated file before committing it.

## Environment Configuration

The application may use environment variables to configure the SQLite database and optional AI settings.

Create a `.env` file in the project root if your application loads configuration from it:

```env
DATABASE_URL=sqlite:///./students.db
```

If the application supports a configurable Ollama model, add the corresponding model setting using the variable name expected by your code.

Do not commit `.env` files containing secrets or private configuration. Commit a `.env.example` file containing only safe example values.

The database URL shown above assumes that the application uses SQLAlchemy's SQLite connection configuration.

## Running the Application

Make sure your virtual environment is activated and that your terminal is in the project root, where `main.py` is located.

Start the development server:

```bash
python -m uvicorn main:app --reload
```

The server should become available at:

- **Base URL:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **OpenAPI schema:** http://127.0.0.1:8000/openapi.json

Keep the terminal running while testing the API. Press `Ctrl+C` to stop the server.

## API Documentation

FastAPI generates interactive documentation from the application's route definitions and request schemas.

Open Swagger UI at:

http://127.0.0.1:8000/docs

From the documentation page, you can:

1. Select an endpoint.
2. Click **Try it out**.
3. Enter query parameters or a JSON request body.
4. Click **Execute**.
5. Review the response code and response body.

Use this interface to demonstrate all four CRUD operations during project evaluation.

## API Endpoints

The following endpoints represent the intended application interface. Use the exact routes and parameter names displayed by your running Swagger documentation if they differ.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/students/` | Create a student |
| GET | `/students/` | List or filter students |
| GET | `/students/{student_id}` | Retrieve a student |
| PUT | `/students/{student_id}` | Update a student |
| DELETE | `/students/{student_id}` | Delete a student |
| POST | `/ai/query-students` | Optional natural-language query |

### Student fields

Student records support the following fields in the current implementation:

| Field | Description |
|---|---|
| `id` | Unique, automatically generated student identifier |
| `student_name` | Student's name |
| `student_dob` | Student's date of birth in `YYYY-MM-DD` format |
| `student_address` | Student's address |
| `student_course` | Student's course |
| `student_section` | Student's section |
| `email` | Student's email address |
| `phone` | Student's contact number |

The assignment requires a unique student ID, name, date of birth, and contact information through email and/or phone. The exact required and optional fields depend on the application's Pydantic schemas.

## Sample API Requests

The examples below illustrate the expected request format. Use them with your running API and adjust any field requirements to match your schemas.

### 1. Create a student

**Request**

```http
POST /students/
Content-Type: application/json
```

**JSON body**

```json
{
  "student_name": "Rahul Sharma",
  "student_dob": "2005-05-15",
  "student_address": "Roorkee",
  "student_course": "B.Tech CSE AI/ML",
  "student_section": "A",
  "email": "rahul.demo@example.com",
  "phone": "9876543210"
}
```

A successful request should return the created student and an appropriate success status.

Use a different email for each new record if email uniqueness is enforced.

### 2. List all students

**Request**

```http
GET /students/
```

This endpoint returns the student records available in the database.

### 3. Retrieve a student by ID

**Request**

```http
GET /students/1
```

Replace `1` with an ID returned by the list endpoint or create response.

If the student does not exist, the API should return HTTP `404 Not Found`.

### 4. Filter students

The application supports filtering using query parameters implemented by the list route.

For example, if the route supports filtering by course:

```http
GET /students/?student_course=B.Tech
```

Other filters may include name, section, and date of birth. Use the actual parameter names shown in Swagger UI.

### 5. Update a student

**Request**

```http
PUT /students/1
Content-Type: application/json
```

**Example JSON body**

```json
{
  "student_name": "Rahul Sharma",
  "student_dob": "2005-05-15",
  "student_address": "Haridwar",
  "student_course": "B.Tech CSE AI/ML",
  "student_section": "B",
  "email": "rahul.demo@example.com",
  "phone": "9876543210"
}
```

Use the request schema shown in Swagger UI. If the endpoint expects all fields, provide a complete valid object. If it supports partial updates, provide only the fields being changed.

### 6. Delete a student

**Request**

```http
DELETE /students/1
```

Replace `1` with an existing student ID.

The API should confirm the deletion using its configured success response. A subsequent request for the deleted record should return `404 Not Found`.

## Database Design

The project uses SQLite for persistent storage and SQLAlchemy to map database records to Python objects.

The student table stores each student's unique ID and personal or academic fields. SQLAlchemy performs database operations through the configured database session.

The database file is generally created automatically when the application initializes its tables, provided that the application has been configured to do so.

Data stored in SQLite persists after the server stops and starts again, as long as the same database file and database URL are used.

## Optional AI Integration with Ollama

The assignment includes an optional bonus feature for natural-language questions about student data.

If the AI extension is enabled, the backend retrieves relevant student records from SQLite and uses those records as context for the language model.

Example questions include:

- How many students are there?
- List students enrolled in B.Tech CSE.
- Which students were born after 2005?

The AI endpoint in this project is:

```http
POST /ai/query-students
```

The exact request body must match the schema displayed in Swagger UI.

### Setting up Ollama

1. Install Ollama from https://ollama.com/.
2. Download the model used by the application. For example:

```bash
ollama pull llama3.2:1b
```

3. Make sure the Ollama service is running.
4. Start the FastAPI application.
5. Open Swagger UI and test the AI endpoint.

The model name configured in the application must match the model installed locally.

**Security note:** The language model should not execute unrestricted SQL. The backend must control database queries and provide retrieved records as context. Use dummy student records for demonstrations and never publish real student personal information.

The core CRUD functionality does not depend on the optional AI feature.

## Testing the API

Use Swagger UI to perform a complete CRUD demonstration.

1. Start the application and open `/docs`.
2. Create a student using `POST /students/`.
3. List students using `GET /students/` and confirm that the new record appears.
4. Retrieve the record by its returned ID.
5. Update the record using `PUT /students/{student_id}`.
6. Retrieve the record again and verify that the changes were saved.
7. Delete the record using `DELETE /students/{student_id}`.
8. Retrieve the deleted record and confirm that the API reports it as missing.
9. Restart the server and verify that other records remain in SQLite.

Also test invalid input, duplicate email addresses if uniqueness is enforced, and requests for nonexistent student IDs.

The project should be considered ready for submission only after these tests pass.

## Error Handling

The API should return meaningful HTTP status codes for common outcomes:

| Status code | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | A resource was created, if configured by the route |
| `204 No Content` | Successful operation with no response body, if configured |
| `404 Not Found` | Requested student does not exist |
| `422 Unprocessable Entity` | Request data failed validation |
| `500 Internal Server Error` | Unexpected server-side error |

Actual success status codes depend on the endpoint implementation.

If an endpoint returns `422`, check the Swagger response body for the `detail` field. It usually identifies a missing field, incorrect data type, or invalid value.

If an endpoint returns `500`, inspect the FastAPI terminal traceback to identify the underlying server-side issue.

## Security Considerations

- Use dummy student data for development and demonstrations.
- Do not commit `.env` files containing secrets.
- Do not upload real student personal information to a public repository.
- Keep database access under backend control.
- Do not allow an AI model to execute unrestricted SQL statements.
- Validate all incoming request data.
- Avoid committing virtual environments, generated bytecode, or unnecessary database files.

## Troubleshooting

### `requirements.txt` not found

Check the files in your project root:

```powershell
Get-ChildItem
```

If your dependency file is named `requirement.txt`, install it with:

```powershell
python -m pip install -r requirement.txt
```

Otherwise, create or restore the appropriate dependency file.

### Virtual environment points to another folder

Deactivate the environment and recreate it inside the current project directory:

```powershell
deactivate
py -3.11 -m venv venv
.\venv\Scripts\Activate.ps1
```

Then install the dependencies again.

### Port 8000 is already in use

Stop the existing server with `Ctrl+C`, or start the application on another port:

```powershell
python -m uvicorn main:app --reload --port 8001
```

### Student endpoint returns 422

Check the validation response in Swagger. Make sure the JSON field names match the current schema, particularly `student_course` and `student_section` if those are the names used by your model.

### Student endpoint returns 404

Check `GET /students/` to confirm that the requested ID exists.

### AI endpoint fails

Check that Ollama is installed, the configured model is available, and the Ollama service is running. CRUD endpoints should still be testable independently of the optional AI extension.

## Author

**Dinesh Baidya**

GitHub: https://github.com/Dinesh-Baidya

Repository: https://github.com/Dinesh-Baidya/EWB_Student_Management_API

Project: Student Management API — EWB Edu Tech Python Backend Development Internship

---

*Developed as an individual backend development project to demonstrate REST API design, database integration, CRUD operations, validation, and optional local AI integration.*
