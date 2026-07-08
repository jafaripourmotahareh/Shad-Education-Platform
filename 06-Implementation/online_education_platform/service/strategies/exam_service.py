online_education_platform/service/exam_service.py

from datetime import datetime from domain.exam import Submission class ExamService:
  def init(self, exam_repository, submission_repository, grade_service):
    self.exam_repository = exam_repository self.submission_repository = submission_repository self.grade_service = grade_service 
    def createExam(self, exam):
      return self.exam_repository.save(exam) 
      def startExam(self, examId): exam = self.exam_repository.findById(examId)
        if exam is None: raise ValueError("Exam not found")
          return exam 
      def submitAnswers(self, examId, studentId, answers): exam = self.exam_repository.findById(examId)
        if exam is None: raise ValueError("Exam not found") 
          submission = Submission(examId=examId, studentId=studentId, answers=answers) 
      submission.submit(submittedAt=datetime.now())#ذخیره نهایی در ریپازیتوری سابمیشن‌ها به جای دیکشنری لوکال سرویس 
  self.submission_repository.save(submission) grade = self.grade_service.calculate(submission, exam) 
  return grade
  def getExamStatus(self, examId): exam = self.exam_repository.findById(examId) 
    if exam is None: return None return { "examId": exam.getUdentifier(), "isPublished": exam.isPublished, "remainingTime": exam.getRemainingTime(), } 
