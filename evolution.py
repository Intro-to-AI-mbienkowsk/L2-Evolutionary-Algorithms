from population import Population


class Evolution:
    def __init__(self, population: Population, epochs: int):
        self.population = population
        self.best_specimens = []
        self.epochs = epochs

    def perform_epoch(self):
        self.population.reproduce()
        self.population.mutate()
        return self.population.find_best_specimen()

    def evolve(self):
        for _ in range(self.epochs):
            self.best_specimens.append(self.perform_epoch())
