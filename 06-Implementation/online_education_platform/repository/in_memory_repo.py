from .interfaces import (
    IUserRepository,
    IClassSessionRepository,
    INotificationRepository,
    IExamRepository,
    ISubmissionRepository,
    IEnrollmentRepository,
    ICourseRepository,
)
from domain.user import Student


class UserRepository(IUserRepository):
    def __init__(self):
        self.users = {}  # استفاده از خود UUID به عنوان کلید

    def save(self, user):
        self.users[user.getUdentifier()] = user
        return user

    def findById(self, id):
        return self.users.get(id)

    def findByEmail(self, email):
        for user in self.users.values():
            if user.email == email:
                return user
        return None

    def findAllStudentsByCourse(self, courseId):
        result = []
        for user in self.users.values():
            if isinstance(user, Student) and courseId in user.enrolledCourses:
                result.append(user)
        return result


class ClassSessionRepository(IClassSessionRepository):
    def __init__(self):
        self.sessions = {}

    def save(self, session):
        self.sessions[session.getUdentifier()] = session
        return session

    def findActiveSessions(self):
        return [session for session in self.sessions.values() if session.status == "active"]


class NotificationRepository(INotificationRepository):
    def __init__(self):
        self.notifications = {}

    def save(self, notification):
        self.notifications[notification.getUdentifier()] = notification
        return notification

    def findUnreadByUserId(self, userId):
        return [
            notification
            for notification in self.notifications.values()
            if notification.userId == userId and not notification.IsRead
        ]


class InMemoryExamRepository(IExamRepository):
    def __init__(self):
        self.exams = {}

    def save(self, exam):
        self.exams[exam.getUdentifier()] = exam
        return exam

    def findById(self, id):
        return self.exams.get(id)

    def findUpcomingExams(self):
        return [exam for exam in self.exams.values() if exam.isPublished]


class SubmissionRepository(ISubmissionRepository):  # پیاده‌سازی مخزن Submission
    def __init__(self):
        self.submissions = {}

    def save(self, submission):
        self.submissions[submission.getUdentifier()] = submission
        return submission

    def findById(self, id):
        return self.submissions.get(id)

    def findByStudentAndExam(self, studentId, examId):
        for sub in self.submissions.values():
            if sub.studentId == studentId and sub.examId == examId:
                return sub
        return None


class EnrollmentRepository(IEnrollmentRepository):
    def __init__(self):
        self.enrollments = {}

    def save(self, enrollment):
        key = self._build_key(enrollment.studentId, enrollment.courseId)
        self.enrollments[key] = enrollment
        return enrollment

    def findByStudentAndCourse(self, studentId, courseId):
        key = self._build_key(studentId, courseId)
        return self.enrollments.get(key)

    def _build_key(self, studentId, courseId):
        return (studentId, courseId)  # استفاده از tuple کلیدهای UUID


class CourseRepository(ICourseRepository):
    def __init__(self):
        self.courses = {}

    def save(self, course):
        self.courses[course.getUdentifier()] = course
        return course

    def findById(self, id):
        return self.courses.get(id)

    def findActiveCourses(self):
        # بررسی وضعیت فعال
        return [course for course in self.courses.values() if course.status == "active"]
