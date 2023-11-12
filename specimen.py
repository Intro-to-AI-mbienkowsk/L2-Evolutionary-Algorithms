import numpy as np
from abc import ABC, abstractmethod
import random
from constants import CITIES
import copy


class Specimen(ABC):
    def __init__(self, value: np.ndarray):
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @abstractmethod
    def mutate(self, mutation_params):
        ...

    @staticmethod
    @abstractmethod
    def generate_random():
        ...


class TSPSpecimen(Specimen):
    def __init__(self, value):
        super().__init__(value)

    def mutate(self, mutation_strength: float):
        # Swap cities at random indices (i, j) len(self.value( * strentgh of mutation times
        for _ in range(round(len(self.value) * mutation_strength / 2)):
            i, j = random.randint(0, len(self.value) - 1), random.randint(0, len(self.value) - 1)
            temp = self.value[i].copy()
            self.value[i] = self.value[j]
            self.value[j] = temp

    @staticmethod
    def generate_random():
        return TSPSpecimen(np.array(random.sample(CITIES, k=len(CITIES))))
