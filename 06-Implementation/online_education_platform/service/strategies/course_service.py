online_education_platform/service/course_service.py
from domain.enrollment import Enrollment
class CourseService:
def init(self, course_repository, enrollment_repository, user_repository): 
  self.course_repository = course_repository self.enrollment_repository = enrollment_repository self.user_repository = user_repository
  def enrollStudent(self, studentId, courseId): student = self.user_repository.findById(studentId) course = self.course_repository.findById(courseId) 
  if student is None: raise ValueError("Student not found") 
    if course is None: raise ValueError("Course not found") existing = self.enrollment_repository.findByStudentAndCourse(studentId, courseId) 
if existing is not None: return existing enrollment = Enrollment(studentId, courseId) 
self.enrollment_repository.save(enrollment) 
student.enrollCourse(courseId) 
course.addStudent(studentId) self.user_repository.save(student) 
self.course_repository.save(course) 
return enrollment def getCourseContent(self, courseId): course = self.course_repository.findById(courseId)
  if course is None: return [] return course.getCourseContent() 
