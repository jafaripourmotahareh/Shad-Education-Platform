from abc import ABC, abstractmethod


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByEmail(self, email):
        pass

    @abstractmethod
    def findAllStudentsByCourse(self, courseId):
        pass


class IClassSessionRepository(ABC):
    @abstractmethod
    def save(self, session):
        pass

    @abstractmethod
    def findActiveSessions(self):
        pass


class INotificationRepository(ABC):
    @abstractmethod
    def save(self, notification):
        pass

    @abstractmethod
    def findUnreadByUserId(self, userId):
        pass


class IExamRepository(ABC):
    @abstractmethod
    def save(self, exam):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findUpcomingExams(self):
        pass


class ISubmissionRepository(ABC):
    @abstractmethod
    def save(self, submission):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByStudentAndExam(self, studentId, examId):
        pass


class IEnrollmentRepository(ABC):
    @abstractmethod
    def save(self, enrollment):
        pass

    @abstractmethod
    def findByStudentAndCourse(self, studentId, courseId):
        pass


class ICourseRepository(ABC):
    @abstractmethod
    def save(self, course):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findActiveCourses(self):
        pass
