from src.evolution import Evolution
from src.population import TSPPopulation
from src.constants import (DEFAULT_POPULATION, DEFAULT_MUTATION_STRENGTH,DEFAULT_EPOCHS, DEFAULT_REPRODUCTION,
                           DEFAULT_SUCCESSION, ReproductionMethod, SuccessionMethod)
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import numpy as np


def plot_data(best_vals, average_vals, description):
    if not len(best_vals) == len(average_vals):
        raise ValueError("Values to plot have to be the same in size.")
    x_vals = np.arange(len(best_vals))
    fig = plt.figure(figsize=(11.5, 6))
    plt.subplots_adjust(right=.55, left=.075)
    fig.set_facecolor('lightgrey')
    ax = plt.subplot()
    ax.plot(x_vals, best_vals, color='r', label='Best specimen in each epoch')
    ax.plot(x_vals, average_vals, color='b', label='Average specimen in each epoch')
    ax.set_title('Best and average values of the goal function in each epoch', weight='semibold')
    plt.text(1.05, 0.5, description, transform=plt.gca().transAxes, va='center')
    plt.xlabel('Epoch nr.')
    plt.ylabel('Path length')
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
    parser.add_argument('-repr', type=int, default=DEFAULT_REPRODUCTION,
                        help='reproduction method (1 for Tourney, 2 for weighted tourney)')
    parser.add_argument('-suc', type=int, default=DEFAULT_SUCCESSION,
                        help='succession method (1 - choose n individuals from the superset of parents and offspring,'
                             '2 - set elite, of size specified by --elite-size'
                             '3 - generational')
    parser.add_argument('--elite-size', type=int, default=None,
                        help='Size of the elite (applies only when elite succession is chosen)')
    args = parser.parse_args()
    population = TSPPopulation(mutation_strength=args.s, num_of_specimens=args.p, reproduction_method=ReproductionMethod(args.repr),
                               succession=SuccessionMethod(args.suc), elite_size=args.elite_size)
    evolution = Evolution(population, args.e)
    evolution.evolve()
    description = evolution.generate_description(round(sorted(evolution.best_specimens)[0], 2))
    plot_data(evolution.best_specimens, evolution.average_specimens, description)


if __name__ == '__main__':
    main()
