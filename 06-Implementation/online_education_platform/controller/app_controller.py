class LoginRequest:

    def __init__(self, email, password):
        self.email = email
        self.password = password


class RegisterRequest:

    def __init__(self, user):
        self.user = user


class AppController:

    def __init__(
        self,
        user_repository,
        course_service,
        exam_service,
        notification_service,
    ):
        self.user_repository = user_repository
        self.course_service = course_service
        self.exam_service = exam_service
        self.notification_service = notification_service

    def register(self, req):
        return self.user_repository.save(req.user)

    def login(self, req):
        user = self.user_repository.findByEmail(req.email)

        if user and user.passwordHash == req.password:
            return {
                "token": "dummy-token-session-jwt",
                "userId": user.getUdentifier(),
                "role": user.role,
            }

        return None

    def enrollStudent(self, studentId, courseId):
        return self.course_service.enrollStudent(studentId, courseId)

    def getCourseContent(self, courseId):
        return self.course_service.getCourseContent(courseId)

    def startExam(self, examId):
        return self.exam_service.startExam(examId)

    def submitAnswers(self, examId, studentId, answers):
        return self.exam_service.submitAnswers(
            examId,
            studentId,
            answers,
        )

    def getUnreadNotifications(self, userId):
        return self.notification_service.getUnreadByUserId(userId)