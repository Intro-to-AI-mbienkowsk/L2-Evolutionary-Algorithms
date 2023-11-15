import numpy as np
from src.specimen import Specimen, TSPSpecimen
from src.constants import DEFAULT_POPULATION, DEFAULT_MUTATION_STRENGTH, ReproductionMethod, SuccessionMethod
from abc import ABC, abstractmethod
import random
import statistics
from copy import deepcopy


class Population(ABC):
    def __init__(self,
                 goal_function: callable,
                 specimen_type: type,
                 mutation_strength,
                 specimens: np.ndarray[Specimen],
                 num_of_specimens,
                 reproduction_method: ReproductionMethod,
                 succession: SuccessionMethod,
                 elite_size: int or None):
        self.goal_function = goal_function
        self.specimen_type = specimen_type
        self.mutation_strength = mutation_strength
        if specimens is not None and len(specimens) != num_of_specimens:
            raise ValueError("Population size not equal to num_of_specimens.")
        self.specimens = specimens if specimens is not None else self.generate_random_population(num_of_specimens)
        self.reproduction_method = reproduction_method
        self.succession_method = succession
        if self.succession_method == SuccessionMethod.SET_ELITE:
            self.elite_size = elite_size if elite_size is not None else self.default_elite_size()

    @abstractmethod
    def reproduce(self):
        ...

    def default_elite_size(self):
        return len(self.specimens) // 5

    def succession(self, offspring):
        if self.succession_method == SuccessionMethod.BEST_FROM_SUPERSET:
            superset = [specimen for specimen in self.specimens] + [specimen for specimen in offspring]
            self.specimens = sorted(superset, key=self.goal_function)[:len(self.specimens)]
        elif self.succession_method == SuccessionMethod.SET_ELITE:
            elite = sorted(self.specimens, key=self.goal_function)[:self.elite_size]
            offspring = sorted(offspring, key=self.goal_function)[:-self.elite_size]
            self.specimens = elite + offspring

    def best_specimen_value(self):
        return sorted([self.goal_function(specimen) for specimen in self.specimens])[0]

    def average_goal_function_value(self):
        return statistics.mean([self.goal_function(specimen) for specimen in self.specimens])

    def generate_random_population(self, n) -> np.ndarray:
        return np.array([self.specimen_type.generate_random() for _ in range(n)])

    def mutate(self, specimens):
        for specimen in specimens:
            specimen.mutate(self.mutation_strength)


class TSPPopulation(Population):
    @staticmethod
    def goal_function(specimen: TSPSpecimen):
        return sum([np.linalg.norm(specimen.value[i] - specimen.value[(i + 1) % len(specimen.value)])
                    for i in range(len(specimen.value))])

    def __init__(self,
                 mutation_strength=DEFAULT_MUTATION_STRENGTH,
                 specimens: np.ndarray[Specimen] = None,
                 num_of_specimens=DEFAULT_POPULATION,
                 reproduction_method: ReproductionMethod = ReproductionMethod.TOURNEY,
                 succession: SuccessionMethod = SuccessionMethod.BEST_FROM_SUPERSET,
                 elite_size: int or None = None):
        super().__init__(self.goal_function, TSPSpecimen, mutation_strength, specimens, num_of_specimens,
                         reproduction_method, succession, elite_size)

    def reproduce(self):
        offspring = []
        weights = [self.goal_function(specimen) for specimen in self.specimens] \
            if self.reproduction_method == ReproductionMethod.WEIGHTED_TOURNEY else [1 for _ in self.specimens]

        for _ in range(len(self.specimens)):
            offspring.append(deepcopy(
                sorted(random.choices(self.specimens, k=2, weights=weights), key=self.goal_function)[0]))

        return np.array(offspring)
