from .base_entity import BaseEntity


class User(BaseEntity):
    def __init__(self, email, passwordHash, fullName, phone, role, entity_id=None):
        super().__init__(entity_id)
        self.email = email
        self.passwordHash = passwordHash
        self.fullName = fullName
        self.phone = phone
        self.role = role
        self.lastLogin = None
        self.isActive = True

    def UpdatedProfile(self, name, phone):
        self.fullName = name
        self.phone = phone

    def changeOassword(self, oldPass, newPass):
        if self.passwordHash != oldPass:
            return False

        self.passwordHash = newPass
        return True


class Student(User):
    def __init__(self, email, passwordHash, fullName, phone, entity_id=None):
        super().__init__(
            email,
            passwordHash,
            fullName,
            phone,
            "student",
            entity_id,
        )
        self.enrolledCourses = []

    def enrollCourse(self, courseId):
        if courseId not in self.enrolledCourses:
            self.enrolledCourses.append(courseId)


class Teacher(User):
    def __init__(self, email, passwordHash, fullName, phone, entity_id=None):
        super().__init__(
            email,
            passwordHash,
            fullName,
            phone,
            "teacher",
            entity_id,
        )
        self.courses = []

    def assignCourse(self, courseId):
        if courseId not in self.courses:
            self.courses.append(courseId)


class Admin(User):
    def __init__(self, email, passwordHash, fullName, phone, entity_id=None):
        super().__init__(
            email,
            passwordHash,
            fullName,
            phone,
            "admin",
            entity_id,
        )