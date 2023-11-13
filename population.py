import numpy as np
from specimen import Specimen, TSPSpecimen
from constants import DEFAULT_POPULATION, DEFAULT_MUTATION_STRENGTH, ReproductionMethod, CITIES
from abc import ABC, abstractmethod
import random
import statistics


class Population(ABC):
    def __init__(self,
                 goal_function: callable,
                 specimen_type: type,
                 mutation_strength,
                 specimens: np.ndarray[Specimen],
                 num_of_specimens,
                 reproduction_method: ReproductionMethod,
                 succession: SuccessionMethod):
        self.goal_function = goal_function
        self.specimen_type = specimen_type
        self.mutation_strength = mutation_strength
        if specimens is not None and len(specimens) != num_of_specimens:
            raise ValueError("Population size not equal to num_of_specimens.")
        self.specimens = specimens if specimens is not None else self.generate_random_population(num_of_specimens)
        self.reproduction_method = reproduction_method
        self.succession_method = succession

    @abstractmethod
    def reproduce(self):
        ...

    def succession(self, offspring):
        if self.succession_method == SuccessionMethod.BEST_FROM_SUPERSET:
            superset = [specimen for specimen in self.specimens] + [specimen for specimen in offspring]
            self.specimens = sorted(superset, key=self.goal_function)[:len(self.specimens)]
        else:
            raise NotImplementedError()

    def best_specimen_value(self):
        return sorted([self.goal_function(specimen) for specimen in self.specimens])[0]

    def average_goal_function_value(self):
        return statistics.mean([self.goal_function(specimen) for specimen in self.specimens])

    def generate_random_population(self, n) -> np.ndarray:
        return np.array([self.specimen_type.generate_random() for _ in range(n)])

    def mutate(self):
        for specimen in self.specimens:
            specimen.mutate(self.mutation_strength)


class TSPPopulation(Population):
    @staticmethod
    def goal_function(specimen: TSPSpecimen):
        return sum([np.linalg.norm(specimen.value[i] - specimen.value[i + 1])
                    for i in range(len(specimen.value) - 1)])

    def __init__(self,
                 mutation_strength=DEFAULT_MUTATION_STRENGTH,
                 specimens: np.ndarray[Specimen] = None,
                 num_of_specimens=DEFAULT_POPULATION,
                 reproduction_method: ReproductionMethod = ReproductionMethod.TOURNEY):
        super().__init__(self.goal_function, TSPSpecimen, mutation_strength, specimens, num_of_specimens,
                         reproduction_method)

    def reproduce(self):
        if self.reproduction_method == ReproductionMethod.TOURNEY:
            probs = np.array([1/self.goal_function(specimen) for specimen in self.specimens])
            new_population = []
            for _ in range(len(self.specimens)):
                new_population.append(sorted(
                    random.choices(self.specimens, weights=probs, k=2),
                    key=self.goal_function)[0])
            self.specimens = new_population
