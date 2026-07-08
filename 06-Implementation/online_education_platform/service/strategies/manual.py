from .base import GradingStrategy


class ManualGradingStrategy(GradingStrategy):

    def evaluate(self, submission, exam):
        # نمرات سوالات تشریحی به صورت دستی ثبت شده‌اند.
        return submission.totalObtainedScore