import numpy as np
from abc import ABC, abstractmethod, abstractproperty


class Specimen(ABC):
    def __init__(self, value: np.ndarray):
        self._value = value

    @property
    def value(self):
        return self._value

    @abstractmethod
    def mutate(self, mutation_params):
        ...
