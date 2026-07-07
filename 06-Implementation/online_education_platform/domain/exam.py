from datetime import datetime, timedelta
from .base_entity import BaseEntity


class Question(BaseEntity):
    def __init__(
        self,
        text,
        score,
        questionType,
        correctAnswer=None,
        options=None,
        entity_id=None
    ):
        super().__init__(entity_id)
        self.text = text
        self.score = score
        self.questionType = questionType
        self.correctAnswer = correctAnswer
        self.options = options or []

    def validateAnswer(self, answer):
        return self.correctAnswer == answer


class Submission(BaseEntity):
    def __init__(self, examId, studentId, answers=None, entity_id=None):
        super().__init__(entity_id)
        self.examId = examId
        self.studentId = studentId
        self.answers = answers or {}
        self.totalObtainedScore = 0
        self.autoSubmitted = False
        self.submittedAt = None

    def submit(self, submittedAt=None, autoSubmitted=False):
        self.submittedAt = submittedAt or datetime.now()
        self.autoSubmitted = autoSubmitted


class Grade(BaseEntity):
    def __init__(self, submissionId, score, isPassed, entity_id=None):
        super().__init__(entity_id)
        self.submissionId = submissionId
        self.score = score
        self.isPassed = isPassed


class Exam(BaseEntity):
    def __init__(
        self,
        title,
        courseId,
        durationMinutes,
        startDate,
        totalScore,
        type,
        shuffleQuestion=False,
        entity_id=None
    ):
        super().__init__(entity_id)
        self.title = title
        self.courseId = courseId
        self.durationMinutes = durationMinutes
        self.startDate = startDate
        self.totalScore = totalScore
        self.type = type
        self.shuffleQuestion = shuffleQuestion
        self.questions = []
        self.isPublished = False

    def addQuestion(self, question):
        self.questions.append(question)

    def publishExam(self):
        self.isPublished = True

    def getRemainingTime(self):
        end_time = self.startDate + timedelta(minutes=self.durationMinutes)
        remaining = end_time - datetime.now()
        if remaining.total_seconds() < 0:
            return timedelta(seconds=0)
        return remaining
