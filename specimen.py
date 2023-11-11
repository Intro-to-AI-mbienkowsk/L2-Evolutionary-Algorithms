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
    def mutate(self, mutation_params: dict):
        # Swap cities at random indices (i, j) len(self.value( * strentgh of mutation times
        for _ in range(round(len(self.value)*mutation_params['MUTATION_STRENGTH'])):
            i, j = random.randint(0, len(self.value)), random.randint(0, len(self.value))
            self.value[i], self.value[j] = self.value[j], self.value[i]

    def generate_random(self):
        return np.array(random.shuffle(copy.copy(CITIES)))
