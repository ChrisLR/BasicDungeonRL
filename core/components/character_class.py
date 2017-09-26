from core.components import Component
from bflib.dice import Dice


class CharacterClass(Component):
    NAME = 'character_class'

    def __init__(self, *base_classes):
        super().__init__()
        self.base_classes = base_classes

    def get_hit_dice(self, level):
        levels = (base_class.level_table.get(level) for base_class in self.base_classes)
        hit_dices = [level.largest_hit_dice for level in levels if level] if levels else None
        if not hit_dices:
            return None
        largest_hit_dice = max(hit_dices, key=lambda h: h.sides)
        restrictions = self.host.restrictions
        if restrictions and largest_hit_dice.sides > restrictions.hit_dice_max_size:
            largest_hit_dice = Dice.get_by_sides(restrictions.hit_dice_max_size)

        return largest_hit_dice

    def copy(self):
        return CharacterClass(
            type(*self.base_classes)()
        )
