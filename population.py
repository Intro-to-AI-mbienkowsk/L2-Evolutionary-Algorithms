from specimen import Specimen
from constants import DEFAULT_POPULATION


class Population:
    def __init__(self,
                 goal_function: callable,
                 crossbreeding_algorithm,
                 specimen_type: type,
                 specimens: list[Specimen] = None,
                 num_of_specimens=DEFAULT_POPULATION):
        ...
