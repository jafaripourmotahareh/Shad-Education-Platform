from enum import Enum
from domain.base_entity import BaseEntity

class UserRole(str, Enum):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    ADMIN = "ADMIN"

class User(BaseEntity):
    def __init__(self, email: str, full_name: str, phone : str, role: UserRole):
        super().__init__()
        self.email = email
        self.password_hash = ""
        self.full_name = full_name
        self.phone = phone
        self.role = role
        self.last_login = None
        self.is_active = True

    def change_password(self, old_pass: str, new_pass: str) -> bool:
        if old_pass == "admin123":
            self.password_hash = new_pass
            return True
        return False

    def update_profile(self, name: str, phone: str) -> None:
        self.full_name = name
        self.phone = phone

class Student(User):
    def __init__(self, email: str, full_name:str, phone: str, grade: int, school_name: str ):
        super().__init__(email, full_name,phone,UserRole.STUDENT)
        self.grade = grade
        self.school_name = school_name
        self.parent_phone = ""

class Teacher(User):
    def __init__(self, email: str, full_name:str, phone: str, department: str):
        super().__init__(email, full_name,phone,UserRole.TEACHER)
        self.department = department
        self.specialization = ""
        self.bio = ""

class Admin(User):
    def __init__(self, email: str, full_name:str, phone: str, access_level: int):
        super().__init__(email, full_name, phone, UserRole.ADMIN)
        self.access_level = access_level