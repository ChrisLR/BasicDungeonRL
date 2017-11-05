from bflib.movement import MovementSet
from bflib.units import FeetPerGameTurn
from core.components.base import Component


class Movement(Component):
    NAME = "movement"
    __slots__ = ["movement_set"]

    def __init__(self, movement_set=None):
        super().__init__()
        self.movement_set = movement_set if movement_set else MovementSet(FeetPerGameTurn(40))

    def speed(self):
        # TODO The speed has to be adjusted by equipment_weight
        pass

    def copy(self):
        return Movement(self.movement_set)
