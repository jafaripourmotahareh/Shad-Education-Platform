from abc import ABC, abstractmethod


class GradingStrategy(ABC):
    @abstractmethod
    def evaluate(self, submission, exam):
        pass
