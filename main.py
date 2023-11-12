from evolution import Evolution
from specimen import TSPSpecimen
from population import TSPPopulation
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
    plt.show()



