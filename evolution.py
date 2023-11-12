from population import Population


class Evolution:
    def __init__(self, population: Population, epochs: int):
        self.population = population
        self.best_specimens = []
        self.average_specimens = []
        self.epochs = epochs

    def perform_epoch(self):
        self.population.reproduce()
        self.population.mutate()
        return self.population.find_best_specimen(), self.population.average_goal_function_value()

    def evolve(self):
        for _ in range(self.epochs):
            best, avg = self.perform_epoch()
            self.best_specimens.append(best)
            self.average_specimens.append(avg)
