from evolution import Evolution
from population import TSPPopulation
from constants import DEFAULT_POPULATION, DEFAULT_MUTATION_STRENGTH, DEFAULT_EPOCHS
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import numpy as np


def plot_data(best_vals, average_vals=None):
    if not len(best_vals) == len(average_vals):
        raise ValueError("Values to plot have to be the same in size.")
    x_vals = np.arange(len(best_vals))
    ax = plt.subplot()
    ax.plot(x_vals, best_vals, color='r', label='Best specimen in each epoch')
    if average_vals is not None:
        ax.plot(x_vals, average_vals, color='b', label='Average specimen in each epoch')
        ax.set_title('Best and average values of the goal function in each epoch')
    else:
        ax.set_title('Best value of the goal function in each epoch')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    parser = ArgumentParser(description='Find optimal route for TSP using an evolutional algorithm.')
    parser.add_argument('-p', type=int, default=DEFAULT_POPULATION,
                        help='size of the population, int')
    parser.add_argument('-s', type=float, default=DEFAULT_MUTATION_STRENGTH,
                        help='mutation strength between 0 and 1, float')
    parser.add_argument('-e', type=int, default=DEFAULT_EPOCHS,
                        help='number of epochs to perform, int')
    # todo: reproduction method
    # todo: make average_specimens optional
    args = parser.parse_args()
    population = TSPPopulation(mutation_strength=args.s, num_of_specimens=args.p)
    evolution = Evolution(population, args.e)
    evolution.evolve()
    plot_data(evolution.best_specimens, evolution.average_specimens)


if __name__ == '__main__':
    main()