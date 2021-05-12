import random

from interfaces.SentenceTransformation import SentenceTransformation
from common.NumericalTransformation import NumericalTransformation
from tasks.TaskTypes import TaskType


class ReplaceNumericalValues(SentenceTransformation):
    tasks = [TaskType.TEXT_CLASSIFICATION, TaskType.TEXT_TO_TEXT_GENERATION]
    locales = ["en"]

    def __init__(self):
        random.seed(10)
        super().__init__()
        self.numerical_transformation = NumericalTransformation()

    def generate(self, sentence: str):
        result = self.numerical_transformation.transform(sentence)

        print(f"Perturbed Input from {self.name()} : {result}")
        return result
