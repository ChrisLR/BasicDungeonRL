from bflib import dice
from core.components import Component, listing


@listing.register
class SavingThrows(Component):
    NAME = "saving_throws"
    __slots__ = ["saving_throws_set"]

    def __init__(self, saving_throws_set):
        super().__init__()
        self.saving_throws_set = saving_throws_set

    def make(self, saving_throw):
        score = self.saving_throws_set.get(saving_throw)
        roll = dice.D20(1).roll_total()
        if roll >= score:
            return True

        return False

    def copy(self):
        return SavingThrows(self.saving_throws_set)
