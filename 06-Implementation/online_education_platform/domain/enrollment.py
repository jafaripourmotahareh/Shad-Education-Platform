from datetime import datetime

from .base_entity import BaseEntity


class Enrollment(BaseEntity):
    def __init__(self, studentId, courseId, entity_id=None):
        super().__init__(entity_id)
        self.studentId = studentId
        self.courseId = courseId
        self.enrolledAt = datetime.now()
        self.ProgressPercent = 0
        self.status = "active"

    def updateProgress(self, percent):
        if percent < 0:
            percent = 0

        if percent > 100:
            percent = 100

        self.ProgressPercent = percent

    def cancel(self):
        self.status = "cancelled"