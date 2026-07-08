online_education_platform/service/grade_service.py

from domain.exam import Grade class GradeService: 
def init(self, strategy=None, passThreshold=50):
  self.strategy = strategy self.passThreshold = passThreshold حد نصاب به صورت درصد (مثلاً 50 یعنی 50٪ کل نمره) 
  def set_strategy(self, strategy): self.strategy = strategy
    def calculate(self, submission, exam):
      if self.strategy is None: raise ValueError("Grading strategy has not been set.")
        score = self.strategy.evaluate(submission, exam) محاسبه آستانه قبولی بر اساس درصد مشخص شده از کل نمره امتحان pass_required_score = exam.totalScore 
      (self.passThreshold / 100.0) is_passed = score >= pass_required_score
      return Grade( submissionId=submission.getUdentifier(), score=score, isPassed=is_passed ) 
