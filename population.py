import numpy as np
from specimen import Specimen, TSPSpecimen
from constants import DEFAULT_POPULATION, MUTATION_STRENGTH, ReproductionMethod, CITIES
from abc import ABC, abstractmethod
import statistics


class Population(ABC):
    def __init__(self,
                 goal_function: callable,
                 specimen_type: type,
                 mutation_strength,
                 specimens: np.ndarray[Specimen],
                 num_of_specimens,
                 reproduction_method: ReproductionMethod):
        self.goal_function = goal_function
        self.specimen_type = specimen_type
        self.mutation_strength = mutation_strength
        if specimens is not None and len(specimens) != num_of_specimens:
            raise ValueError("Population size not equal to num_of_specimens.")
        self.specimens = specimens if specimens is not None else self.generate_random_population(num_of_specimens)
        self.reproduction_method = reproduction_method

    @abstractmethod
    def reproduce(self):
        ...

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
                    for i in range(len(specimen.value))])

    def __init__(self,
                 mutation_strength=MUTATION_STRENGTH,
                 specimens: np.ndarray[Specimen] = None,
                 num_of_specimens=DEFAULT_POPULATION,
                 reproduction_method: ReproductionMethod = ReproductionMethod.TOURNEY):
        super().__init__(self.goal_function, TSPSpecimen, mutation_strength, specimens, num_of_specimens,
                         reproduction_method)

    def reproduce(self):
        if self.reproduction_method == ReproductionMethod.TOURNEY:
            fitness = self.goal_function(self.specimens)
            # normalize probabilities
            probs = fitness/np.sum(fitness)
            new_population = []
            for i in range(len(self.specimens)):
                new_population.append(sorted(
                    [np.random.choice(self.specimens, p=fitness, size=2)],
                    key=self.goal_function))
            self.specimens = new_population
