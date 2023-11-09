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
        ...

    def generate_random(self):
        return np.array(random.shuffle(copy.copy(CITIES)))