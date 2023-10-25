from specimen import Specimen


class Population:
    def __init__(self, specimens: list[Specimen], num_of_specimens: int, specimen_type: type):
        self._specimens = specimens if specimens is not None else [specimen_type() for i in range(num_of_specimens)]
