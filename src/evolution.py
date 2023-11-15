from src.population import Population


class Evolution:
    def __init__(self, population: Population, epochs: int):
        self.population = population
        self.best_specimens = []
        self.average_specimens = []
        self.epochs = epochs

    def perform_epoch(self):
        offspring = self.population.reproduce()
        self.population.mutate(offspring)
        self.population.succession(offspring)
        return self.population.best_specimen_value(), self.population.average_goal_function_value()

    def evolve(self):
        for _ in range(self.epochs):
            best, avg = self.perform_epoch()
            self.best_specimens.append(best)
            self.average_specimens.append(avg)
