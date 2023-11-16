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

    def generate_description(self, best_val):
        title = "Parameters:\n"
        best = f"Best specimen out of all epochs reached the path length of {best_val}\n"
        pop_message = f"Population size: {len(self.population.specimens)}\n"
        mutation_message = f"Mutation strength: {self.population.mutation_strength}\n"
        num_epochs = f"Number of epochs: {self.epochs}\n"
        repr_method = self.population.generate_reproduction_description()
        succession = self.population.generate_succession_description()
        return title + best + pop_message + mutation_message + num_epochs + repr_method + succession
