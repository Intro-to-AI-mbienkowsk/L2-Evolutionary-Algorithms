import numpy as np

from specimen import Specimen, TSPSpecimen
from constants import DEFAULT_POPULATION, MUTATION_STRENGTH, ReproductionMethod
from abc import ABC, abstractmethod


class Population(ABC):
    def __init__(self,
                 goal_function: callable,
                 specimen_type: type,
                 mutation_strength,
                 specimens: list[Specimen],
                 num_of_specimens,
                 reproduction_method: ReproductionMethod):
        self.goal_function = goal_function
        self.specimen_type = specimen_type
        self.mutation_strength = mutation_strength
        if specimens is not None and len(specimens != num_of_specimens):
            raise ValueError("Population size not equal to num_of_specimens.")
        self.specimens = specimens if specimens is not None else self.generate_random_population(num_of_specimens)
        self.reproduction_method = reproduction_method

    @abstractmethod
    def reproduce(self):
        ...

    def find_best_specimen(self):
        return sorted(self.specimens, key=self.goal_function)[0]

    def generate_random_population(self, n) -> np.ndarray:
        return np.array([self.specimen_type.generate_random() for _ in range(n)])


class TSPPopulation(Population):
    @staticmethod
    def goal_function(specimen):
        ...

    def __init__(self,
                 mutation_strength=MUTATION_STRENGTH,
                 specimens: list[Specimen] = None,
                 num_of_specimens=DEFAULT_POPULATION,
                 reproduction_method: ReproductionMethod = ReproductionMethod.TOURNEY):
        super().__init__(self.goal_function, TSPSpecimen, mutation_strength, specimens, num_of_specimens,
                         reproduction_method)

    def reproduce(self):
        if self.reproduction_method == ReproductionMethod.TOURNEY:
            ...
