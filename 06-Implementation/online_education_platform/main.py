from datetime import datetime, timedelta

from controller.app_controller import (
    AppController,
    RegisterRequest,
    LoginRequest,
)

from domain.course import Course, Content
from domain.exam import Exam, Question
from domain.user import Student, Teacher

from repository.in_memory_repo import (
    UserRepository,
    NotificationRepository,
    InMemoryExamRepository,
    SubmissionRepository,
    EnrollmentRepository,
    CourseRepository,
)

from service.course_service import CourseService
from service.exam_service import ExamService
from service.grade_service import GradeService
from service.notification_service import NotificationService

from service.strategies.auto import AutoGradingStrategy
from service.strategies.late_penalty import LatePenaltyDecorator


def main():

    # -----------------------------
    # Repositories
    # -----------------------------

    user_repository = UserRepository()
    course_repository = CourseRepository()
    enrollment_repository = EnrollmentRepository()
    exam_repository = InMemoryExamRepository()
    submission_repository = SubmissionRepository()
    notification_repository = NotificationRepository()

    # -----------------------------
    # Services
    # -----------------------------

    course_service = CourseService(
        course_repository=course_repository,
        enrollment_repository=enrollment_repository,
        user_repository=user_repository,
    )

    # Strategy + Decorator

    base_strategy = AutoGradingStrategy()

    penalty_strategy = LatePenaltyDecorator(
        base_strategy,
        penalty_percent=0.10,
    )

    grade_service = GradeService(
        strategy=penalty_strategy,
        passThreshold=50,
    )

    exam_service = ExamService(
        exam_repository=exam_repository,
        submission_repository=submission_repository,
        grade_service=grade_service,
    )

    notification_service = NotificationService(
        notification_repository=notification_repository
    )

    # -----------------------------
    # Controller
    # -----------------------------

    app_controller = AppController(
        user_repository=user_repository,
        course_service=course_service,
        exam_service=exam_service,
        notification_service=notification_service,
    )

    # -----------------------------
    # Test Scenario
    # -----------------------------

    teacher = Teacher(
        email="teacher@example.com",
        passwordHash="1234",
        fullName="Professor Smith",
        phone="09120000000",
    )

    student = Student(
        email="student@example.com",
        passwordHash="1234",
        fullName="John Doe",
        phone="09121111111",
    )

    app_controller.register(RegisterRequest(teacher))
    app_controller.register(RegisterRequest(student))

    # -----------------------------
    # Course
    # -----------------------------

    course = Course(
        title="Software Architecture",
        description="Introduction to Design Patterns & DDD",
        teacherId=teacher.getUdentifier(),
        startDate=datetime.now(),
        endDate=datetime.now() + timedelta(days=30),
        status="active",
    )

    course.addContent(
        Content(
            "Lecture 1: Repository Pattern",
            "pdf",
            "repo.pdf",
        )
    )

    course_repository.save(course)

    # Student Enrollment

    app_controller.enrollStudent(
        student.getUdentifier(),
        course.getUdentifier(),
    )

    # -----------------------------
    # Exam
    # -----------------------------

    exam = Exam(
        title="Quiz on Strategy Pattern",
        courseId=course.getUdentifier(),
        durationMinutes=15,
        startDate=datetime.now(),
        totalScore=100,
        type="mixed",
        shuffleQuestion=False,
    )

    q1 = Question(
        text="Which pattern belongs to behavioral patterns?",
        score=60,
        questionType="objective",
        correctAnswer="Strategy",
        options=[
            "Factory",
            "Strategy",
            "Adapter",
        ],
    )

    q2 = Question(
        text="Explain DDD Aggregate Root in detail.",
        score=40,
        questionType="subjective",
        correctAnswer=None,
    )

    exam.addQuestion(q1)
    exam.addQuestion(q2)

    exam.publishExam()

    exam_repository.save(exam)

    # -----------------------------
    # Student Answers
    # -----------------------------

    answers = {
        q1.getUdentifier(): "Strategy",
        q2.getUdentifier(): "An Aggregate Root is...",
    }

    grade = app_controller.submitAnswers(
        examId=exam.getUdentifier(),
        studentId=student.getUdentifier(),
        answers=answers,
    )

    # -----------------------------
    # Output
    # -----------------------------

    print("\n--- Results Output ---")

    print(f"Base Auto Score (Objective): {60} / 100")
    print(f"Score after 10% Late Penalty: {grade.score} / 100")
    print(f"Is Passed (>= 50% threshold): {grade.isPassed}")

    login_result = app_controller.login(
        LoginRequest(
            "student@example.com",
            "1234",
        )
    )

    print("User Login Verification (ID):", login_result["userId"])


if __name__ == "__main__":
    main()