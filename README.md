# Assignment Portal (Flask)

A complete Flask-based Assignment Management System for Teachers and
Students.

## Features

-   User Registration & Login
-   Roles: Teacher & Student
-   Teachers can create assignments
-   Students can submit assignments
-   Teachers can view submissions
-   File upload support
-   SQLite Database
-   Bootstrap UI templates

## Project Structure

    assignment_portal/
    │
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── instance/
    │   └── assignment_portal.db
    │
    ├── static/
    │   ├── css/
    │   └── uploads/
    │
    ├── templates/
    │   ├── base.html
    │   ├── index.html
    │   ├── login.html
    │   ├── register.html
    │   ├── dashboard.html
    │   ├── create_assignment.html
    │   ├── submit_assignment.html
    │   └── submissions.html
    │
    └── models.py

## Installation

### 1. Create Virtual Environment

    python3 -m venv venv
    source venv/bin/activate

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Initialize Database

    flask --app app.py init-db

### 4. Run Server

    flask run

Now open:\
`http://127.0.0.1:5000/`

## Roles

### 👨‍🏫 Teacher

-   Create assignments
-   View all student submissions

### 👨‍🎓 Student

-   View assignments
-   Upload submissions

## File Uploads

Uploaded files are stored in:

    static/uploads/

## Tech Stack

-   Flask
-   SQLite
-   SQLAlchemy
-   Flask-Login
-   Bootstrap

