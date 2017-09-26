from core.components.base import Component
from bflib.movement import MovementSet
from bflib.units import FeetPerGameTurn


class Movement(Component):
    NAME = "movement"

    def __init__(self, movement_set=None):
        super().__init__()
        self.movement_set = movement_set if movement_set else MovementSet(FeetPerGameTurn(40))

    def speed(self):
        # TODO The speed has to be adjusted by equipment_weight
        pass

    def copy(self):
        return Movement()
