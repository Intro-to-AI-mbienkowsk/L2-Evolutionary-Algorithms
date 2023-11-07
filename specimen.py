import numpy as np
from abc import ABC, abstractmethod


class Specimen(ABC):
    def __init__(self, value: np.ndarray):
        self._value = value

    @property
    def value(self):
        return self._value

    @abstractmethod
    def mutate(self, mutation_params):
        ...

    @staticmethod
    @abstractmethod
    def generate_random():
        ...


class TSPSpecimen(Specimen):
    def mutate(self, mutation_params):
        pass

    def generate_random(self):
        pass
