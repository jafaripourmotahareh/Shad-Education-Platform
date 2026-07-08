from .base_entity import BaseEntity


class Content(BaseEntity):
    def __init__(self, title, contentType, data, entity_id=None):
        super().__init__(entity_id)
        self.title = title
        self.contentType = contentType
        self.data = data


class Course(BaseEntity):
    def __init__(
        self,
        title,
        description,
        teacherId,
        startDate,
        endDate,
        status="draft",
        entity_id=None,
    ):
        super().__init__(entity_id)
        self.title = title
        self.description = description
        self.teacherId = teacherId
        self.startDate = startDate
        self.endDate = endDate
        self.status = status
        self.contents = []
        self.enrolledStudents = []

    def addContent(self, content):
        self.contents.append(content)

    def getCourseContent(self):
        return list(self.contents)

    def addStudent(self, studentId):
        if studentId not in self.enrolledStudents:
            self.enrolledStudents.append(studentId)

    def getEnrolledStudents(self):
        return list(self.enrolledStudents)
