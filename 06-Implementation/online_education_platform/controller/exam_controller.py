"""
Exam Controller

Acts as the interface between the presentation layer and the service layer.
This controller contains no business logic and delegates all operations
to the ExamService.
"""

from __future__ import annotations

import uuid
from typing import Any


class ExamController:
    """
    Controller responsible for exam-related operations.
    """

    def __init__(self, exam_service: Any):
        """
        Initialize the controller.

        Args:
            exam_service: Instance of ExamService.
        """
        self._exam_service = exam_service

    def start_exam(
        self,
        exam_id: uuid.UUID,
        student_id: uuid.UUID,
    ) -> dict:
        """
        Start an exam for a student.

        Args:
            exam_id: Exam identifier.
            student_id: Student identifier.

        Returns:
            Standard response dictionary.
        """
        try:
            submission = self._exam_service.start_exam(
                exam_id,
                student_id,
            )

            return {
                "success": True,
                "message": "Exam started successfully.",
                "data": submission,
            }

        except ValueError as error:
            return {
                "success": False,
                "message": str(error),
                "data": None,
            }

        except Exception as error:
            return {
                "success": False,
                "message": f"Unexpected error: {error}",
                "data": None,
            }

    def submit_answer(
        self,
        submission_id: uuid.UUID,
        question_id: uuid.UUID,
        answer_text: str,
    ) -> dict:
        """
        Submit an answer for a question.

        Args:
            submission_id: Submission identifier.
            question_id: Question identifier.
            answer_text: Student answer.

        Returns:
            Standard response dictionary.
        """
        try:
            answer = self._exam_service.submit_answer(
                submission_id,
                question_id,
                answer_text,
            )

            return {
                "success": True,
                "message": "Answer submitted successfully.",
                "data": answer,
            }

        except ValueError as error:
            return {
                "success": False,
                "message": str(error),
                "data": None,
            }

        except Exception as error:
            return {
                "success": False,
                "message": f"Unexpected error: {error}",
                "data": None,
            }