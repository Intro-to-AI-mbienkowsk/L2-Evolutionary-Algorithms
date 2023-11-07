from enum import Enum

DEFAULT_POPULATION = 100
CROSSBREEDING_PROBABILITY = 0.4
MUTATION_STRENGTH = 0.2

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


class CrossbreedingAlgorithm(Enum):
    SINGLE_POINT = 1
    DOUBLE_POINT = 2
