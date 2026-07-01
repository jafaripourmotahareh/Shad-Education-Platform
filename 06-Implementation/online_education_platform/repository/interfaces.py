from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from domain.user import User
from domain.course import Course, Enrollment
from domain.exam import Exam
from domain.notification import Notification
from domain.exam import ExamSubmission
from domain.exam import Grade


# =========================
# USER REPOSITORY
# =========================
class IUserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def find_all_students_by_course(self, course_id: UUID) -> List[User]:
        pass


# =========================
# COURSE REPOSITORY
# =========================
class ICourseRepository(ABC):

    @abstractmethod
    def save(self, course: Course) -> Course:
        pass

    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[Course]:
        pass

    @abstractmethod
    def find_active_courses(self) -> List[Course]:
        pass


# =========================
# NOTIFICATION REPOSITORY
# =========================
class INotificationRepository(ABC):

    @abstractmethod
    def save(self, notification: Notification) -> Notification:
        pass

    @abstractmethod
    def find_unread_by_user_id(self, user_id: UUID) -> List[Notification]:
        pass


# =========================
# EXAM REPOSITORY
# =========================
class IExamRepository(ABC):

    @abstractmethod
    def save(self, exam: Exam) -> Exam:
        pass

    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[Exam]:
        pass

    @abstractmethod
    def find_upcoming_exams(self) -> List[Exam]:
        pass


# =========================
# CLASS SESSION REPOSITORY
# =========================
class IClassSessionRepository(ABC):

    @abstractmethod
    def save(self, session) -> object:
        pass

    @abstractmethod
    def find_active_sessions(self) -> List:
        pass


# =========================
# ENROLLMENT REPOSITORY
# =========================
class IEnrollmentRepository(ABC):

    @abstractmethod
    def save(self, enrollment: Enrollment) -> Enrollment:
        pass

    @abstractmethod
    def find_by_student_and_course(
        self,
        student_id: UUID,
        course_id: UUID
    ) -> Optional[Enrollment]:
        pass
