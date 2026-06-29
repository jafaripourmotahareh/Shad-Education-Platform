import uuid
from typing import List, Dict
from datetime import datetime
from enum import Enum
from domain.base_entity import BaseEntity

class ExamType(str, Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

class QuestionType(str, Enum):
    MCQ = "MCQ"
    TRUE_FALSE = "TRUE_FALSE"
    ESSAY = "ESSAY"
    NUMERIC = "NUMERIC"

class Exam(BaseEntity):
    # سازنده با ۳ پارامتر: title, course_id, duration_minutes
    def __init__(self, title: str, course_id: uuid.UUID, duration_minutes: int):
        super().__init__()
        self.title = title
        self.course_id = course_id
        self.duration_minutes = duration_minutes
        self.total_score = 0.0
        self.type = ExamType.ONLINE
        self.shuffle_questions = False
        self._questions: List['Question'] = []

    def publish_exam(self) -> None:
        pass

class Question(BaseEntity):
    def __init__(self, exam_id: uuid.UUID, text: str, q_type: QuestionType, score: float):
        super().__init__()
        self.exam_id = exam_id

        self.question_text = text
        self.type = q_type
        self.score = score
        self.options_json = "{}"
        self.correct_answer = ""

    def validate_answer(self, answer: str) -> bool:
        if self.type in [QuestionType.MCQ, QuestionType.TRUE_FALSE]:
            return answer.strip().upper() == self.correct_answer.strip().upper()
        if self.type == QuestionType.NUMERIC:
            try:
                return float(answer) == float(self.correct_answer)
            except ValueError:
                return False
        return False

class ExamSubmission(BaseEntity):
    def __init__(self, exam_id: uuid.UUID, student_id: uuid.UUID):
        super().__init__()
        self.exam_id = exam_id
        self.student_id = student_id
        self.start_time = datetime.now()
        self.end_time = None
        self.is_auto_submitted = False
        self.total_obtained_score = 0.0
        self._answers: List['Answer'] = []

    def submit_answers(self, answers: Dict[uuid.UUID, str]) -> None:
        for q_id, ans_text in answers.items():
            ans = Answer(submission_id=self.id, question_id=q_id, given_answer=ans_text)
            self._answers.append(ans)
        self.end_time = datetime.now()

class Answer(BaseEntity):
    def __init__(self, submission_id: uuid.UUID, question_id: uuid.UUID,

given_answer: str):
        super().__init__()
        self.submission_id = submission_id
        self.question_id = question_id
        self.given_answer = given_answer
        self.obtained_score = 0.0
        self.is_correct = False

    def grade_answer(self, correct_answer: str) -> None:
        if self.given_answer.strip().upper() == correct_answer.strip().upper():
            self.is_correct = True
            self.obtained_score = 1.0

class Grade(BaseEntity):
    def __init__(self, submission_id: uuid.UUID, scorer_id: uuid.UUID, score: float):
        super().__init__()
        self.submission_id = submission_id
        self.scorer_id = scorer_id
        self.score = score
        self.feedback = ""
        self.graded_at = datetime.now()
