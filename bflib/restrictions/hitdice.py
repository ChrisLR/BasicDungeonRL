from bflib.restrictions.base import Restriction
from bflib.util import max_if


class HitDiceMaxSizeRestriction(Restriction):
    __slots__ = ["hit_dice_max_size"]

    def __init__(self, hit_dice_max_size):
        self.hit_dice_max_size = hit_dice_max_size

    @classmethod
    def from_merge(cls, first, other):
        cls(
            hit_dice_max_size=max_if(
                first.hit_dice_max_size, other.hit_dice_max_size)
        )

    @property
    def dice(self):
        return self.hit_dice_max_size
