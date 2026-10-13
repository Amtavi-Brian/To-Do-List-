# 📝 To-Do List API

A RESTful To-Do List API built with **FastAPI, PostgreSQL, SQLAlchemy, and Alembic**. The project provides a backend foundation for managing tasks and developing user authentication.

This project focuses on learning backend development, REST API design, relational database management, database migrations, and secure password handling.

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Architecture](#-project-architecture)
- [Database Models](#-database-models)
- [Getting Started](#-getting-started)
- [Database Setup](#-database-setup)
- [Running the Application](#-running-the-application)
- [API Documentation](#-api-documentation)
- [Environment Variables](#-environment-variables)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 🚀 Overview

The To-Do List API is a backend application designed to manage tasks through HTTP requests.

It uses FastAPI to expose API endpoints, PostgreSQL to store application data, SQLAlchemy to interact with the database, and Alembic to manage database schema changes.

The project also includes user-related schemas and password hashing and verification work, providing a foundation for authentication functionality.

The API can be tested independently using its interactive documentation, without requiring a frontend or mobile application.

## ✨ Features

### Task Management

- Store tasks in a PostgreSQL database.
- Track task completion status.
- Record task creation timestamps.
- Validate incoming data using Pydantic schemas.
- Support task creation, retrieval, and updates through the API as implemented.

### Database Management

- PostgreSQL relational database.
- SQLAlchemy ORM.
- Alembic database migrations.
- Version-controlled database schema changes.
- A `created_at` field for recording when tasks were created.

### Authentication Development

- User creation and response schemas.
- Password hashing and verification testing using Argon2.
- Foundation for implementing secure user authentication.

> Authentication features and individual CRUD endpoints should be verified against the current source code before being described as fully implemented.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| PostgreSQL | Relational database |
| SQLAlchemy | Database ORM |
| Alembic | Database migrations |
| Pydantic | Request and response validation |
| Argon2 | Password hashing and verification |
| Uvicorn | ASGI server |
| Git and GitHub | Version control |

## 🏗️ Project Architecture

```text
Client / API Testing Tool
          |
          | HTTP Requests
          v
+------------------------+
|       FastAPI          |
|    API Endpoints       |
|  Request Validation    |
|  Application Logic     |
+------------------------+
          |
          v
+------------------------+
|      SQLAlchemy        |
|       ORM Layer        |
+------------------------+
          |
          v
+------------------------+
|      PostgreSQL        |
|        todo_db         |
+------------------------+

Alembic: Database Schema Migrations
```

The backend can be accessed through Swagger UI or any compatible HTTP client.

## 🗄️ Database Models

### Todo

The `todos` table contains the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | Integer | Primary key identifying a task |
| `title` | String | Task title |
| `completed` | Boolean | Indicates whether the task is completed |
| `created_at` | DateTime | Records when the task was created |

The `title` field was configured as nullable in the model developed so far.

### User

The project also includes user-related schemas for handling user data. The final database fields and authentication relationships should be documented according to the current implementation.

## ⚙️ Getting Started

### Prerequisites

Install the following:

- Python
- PostgreSQL
- Git
- A terminal or code editor such as VS Code

The instructions below are intended for a local development environment on Linux, including Arch Linux.

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_DIRECTORY>
```

Replace the placeholders with your actual repository URL and directory name.

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If your repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies specified by your existing project configuration.

## 🐘 Database Setup

Make sure PostgreSQL is running.

On Arch Linux:

```bash
sudo systemctl enable --now postgresql
```

Create the application database using a PostgreSQL account with appropriate privileges:

```sql
CREATE DATABASE todo_db;
```

Configure your SQLAlchemy connection URL to point to the database:

```text
postgresql://USERNAME:PASSWORD@localhost:5432/todo_db
```

Use the username and password configured on your machine. Avoid committing database credentials to GitHub.

## 🔄 Database Migrations

This project uses Alembic to manage changes to the database schema.

Apply the existing migrations:

```bash
alembic upgrade head
```

Check the current database revision:

```bash
alembic current
```

View the migration history:

```bash
alembic history
```

When making changes to SQLAlchemy models, you can generate a migration with:

```bash
alembic revision --autogenerate -m "describe your changes"
```

Review the generated migration before applying it.

## ▶️ Running the Application

Activate your virtual environment and start the FastAPI server using the correct module path for your project.

For example, if `main.py` contains the FastAPI instance named `app`:

```bash
uvicorn main:app --reload
```

If the application is inside a package, adjust the command accordingly, for example:

```bash
uvicorn app.main:app --reload
```

The development server will usually be available at:

```text
http://127.0.0.1:8000
```

The `--reload` flag automatically restarts the server when source files change.

## 📖 API Documentation

FastAPI generates interactive API documentation automatically when enabled.

After starting the server, visit:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc
- **OpenAPI schema:** http://127.0.0.1:8000/openapi.json

Swagger UI allows you to inspect available endpoints, submit requests, and view API responses directly from your browser.

The actual endpoints and their request formats are determined by the routes implemented in the project.

## 🔐 Environment Variables

Sensitive configuration should be stored in environment variables rather than hard-coded into application files.

Example `.env.example`:

```dotenv
DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost:5432/todo_db
SECRET_KEY=replace_with_a_secure_random_secret
```

Include only variables that your application actually uses. If authentication has not yet been connected to a signing mechanism, `SECRET_KEY` may not currently be required.

Add the following entries to `.gitignore` where applicable:

```gitignore
.env
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
```

Never commit real passwords, tokens, or production secrets.

## 🚧 Future Improvements

Potential improvements include:

- Complete and test user registration and login.
- Implement token-based authentication if required.
- Associate tasks with individual users.
- Add task deletion and any remaining CRUD endpoints.
- Add filtering, sorting, pagination, priorities, and due dates.
- Write automated tests using Pytest.
- Improve API error handling and validation.
- Deploy the API and PostgreSQL database.
- Build a frontend or mobile application in the future.

These are possible future enhancements, not claims that the features already exist.

## 👨‍💻 Author

**Brian Amtavi**

BBIT Student | Backend Development Learner

This project represents my ongoing journey in backend development, REST API design, database management, and secure application development.

## 📄 License

No lincense
