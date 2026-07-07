# Online Education Platform

A Python-based online education platform developed using object-oriented programming principles and common software architecture patterns. The project demonstrates a modular architecture with separated domain, service, repository, controller, and event layers.

## Features

- User management (Student, Teacher, Admin)
- Course creation and enrollment
- Course content management
- Online examination system
- Automatic and manual grading
- Late submission penalty using the Decorator pattern
- Event-driven notification mechanism
- In-memory repository implementation
- UUID-based entity identification

## Design Patterns

This project demonstrates the use of several software design patterns:

- Repository Pattern
- Strategy Pattern
- Decorator Pattern
- Observer Pattern
- Dependency Injection

## Project Structure

```
online_education_platform/
│
├── controller/
├── domain/
├── event/
├── repository/
├── service/
│   └── strategies/
├── main.py
└── README.md
```

## Requirements

- Python 3.10 or later
- No external libraries are required.

## Running the Project

Execute the following command:

```bash
python main.py
```

## Example Workflow

The sample scenario executed in `main.py` demonstrates:

1. Creating teacher and student accounts
2. Registering users
3. Creating a course
4. Enrolling a student
5. Creating and publishing an exam
6. Submitting answers
7. Automatic grading
8. Applying the late submission decorator
9. User authentication

## Notes

- Data is stored in memory only.
- Every entity uses a UUID as its identifier.
- Automatic grading is supported for objective questions.
- Subjective questions can be graded manually.
- The passing score is calculated as a configurable percentage of the total exam score.