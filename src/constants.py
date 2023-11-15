import enum

DEFAULT_POPULATION = 100
DEFAULT_MUTATION_STRENGTH = .1
CITIES = [[35, 51],
          [113, 213],
          [82, 280],
          [322, 340],
          [256, 352],
          [160, 24],
          [322, 145],
          [12, 349],
          [282, 20],
          [241, 8],
          [398, 153],
          [182, 305],
          [153, 257],
          [275, 190],
          [242, 75],
          [19, 229],
          [303, 352],
          [39, 309],
          [383, 79],
          [226, 343]
          ]
DEFAULT_EPOCHS = 100


class ReproductionMethod(enum.Enum):
    TOURNEY = 1,
    WEIGHTED_TOURNEY = 2


class SuccessionMethod(enum.Enum):
    BEST_FROM_SUPERSET = 1,
    ELITE = 2

class MutationMethod(enum.Enum):
    SWAP_N_PAIRS = 1,
    SWAP_EACH_ELEM = 2
