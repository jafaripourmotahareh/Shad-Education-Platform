 online_education_platform/service/strategies/late_penalty.py

from .base import GradingStrategy
  class LatePenaltyDecorator(GradingStrategy):
    def init(self, strategy, penalty_percent): 
 self.strategy = strategy 
 self.penalty_percent = penalty_percent  مثلاً 0.10 یعنی 10 درصد

    def evaluate(self, submission, exam):
  base_score = self.strategy.evaluate(submission, exam) 
     if submission.autoSubmitted: final_score = base_score  (1.0 - self.penalty_percent) else:
  final_score = base_score final_score = max(0.0, final_score) 
  submission.totalObtainedScore = final_score
     return final_score 
