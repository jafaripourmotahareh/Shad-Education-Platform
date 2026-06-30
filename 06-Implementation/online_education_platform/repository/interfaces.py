from abc import ABC, abstractmethod
from typing import List, Optional
import uuid

from domain.user import User
from domain.course import Course, Enrollment
from domain.exam import Exam, ExamSubmission, Grade
from domain.notification import Notification


class IUserRepository(ABC):

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: uuid.UUID) -> Optional[User]:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: uuid.UUID) -> None:
        pass


class ICourseRepository(ABC):

    @abstractmethod
    def add(self, course: Course) -> None:
        pass

    @abstractmethod
    def get_by_id(self, course_id: uuid.UUID) -> Optional[Course]:
        pass

    @abstractmethod
    def get_all(self) -> List[Course]:
        pass

    @abstractmethod
    def update(self, course: Course) -> None:
        pass

    @abstractmethod
    def delete(self, course_id: uuid.UUID) -> None:
        pass

    @abstractmethod
    def enroll(self, enrollment: Enrollment) -> None:
        pass

    @abstractmethod
    def get_enrollments(self, course_id: uuid.UUID) -> List[Enrollment]:
        pass


class IExamRepository(ABC):

    @abstractmethod
    def add(self, exam: Exam) -> None:
        pass

    @abstractmethod
    def get_by_id(self, exam_id: uuid.UUID) -> Optional[Exam]:
        pass

    @abstractmethod
    def get_all(self) -> List[Exam]:
        pass

    @abstractmethod
    def update(self, exam: Exam) -> None:
        pass

    @abstractmethod
    def delete(self, exam_id: uuid.UUID) -> None:
        pass

    @abstractmethod
    def save_submission(self, submission: ExamSubmission) -> None:
        pass

    @abstractmethod
    def get_submission(
        self,
        submission_id: uuid.UUID
    ) -> Optional[ExamSubmission]:
        pass

    @abstractmethod
    def save_grade(self, grade: Grade) -> None:
        pass

    @abstractmethod
    def get_grade(
        self,
        submission_id: uuid.UUID
    ) -> Optional[Grade]:
        pass


class INotificationRepository(ABC):

    @abstractmethod
    def add(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def get_by_id(
        self,
        notification_id: uuid.UUID
    ) -> Optional[Notification]:
        pass

    @abstractmethod
    def get_user_notifications(
        self,
        user_id: uuid.UUID
    ) -> List[Notification]:
        pass

    @abstractmethod
    def update(self, notification: Notification) -> None:
        pass

    @abstractmethod
    def delete(self, notification_id: uuid.UUID) -> None:
        pass
