import uuid
from typing import List
from domain.base_entity import BaseEntity

class Course(BaseEntity):
    def __init__(self, title: str, description: str, teacher_id: uuid.UUID):
        super().__init__()
        self.title = title
        self.description = description
        self.teacher_id = teacher_id
        self.status = "DRAFT" #یا باید DRAFT باشه یا PUBLISHED یا ARCHIVED
        self._contents: List = []

        def add_content(self, content) -> None:
            self._contents.append(content)

class Enrollment(BaseEntity):
    def __init__(self, student_id: uuid.UUID, course_id: uuid.UUID):
        super().__init__()
        self.student_id = student_id
        self.course_id = course_id
        self.progress_percent = 0.0
        self.status = "ACTIVE"
