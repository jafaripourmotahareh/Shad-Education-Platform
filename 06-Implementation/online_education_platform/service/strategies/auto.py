from .base import GradingStrategy


class AutoGradingStrategy(GradingStrategy):

    def evaluate(self, submission, exam):
        total = 0

        for question in exam.questions:
            # تصحیح خودکار فقط برای سوالات تستی
            if question.questionType == "objective":
                answer = submission.answers.get(question.getUdentifier())

                if question.validateAnswer(answer):
                    total += question.score

        submission.totalObtainedScore = total
        return total