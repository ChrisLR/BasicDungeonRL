from bflib.dice import Dice
from core.components import Component


class CharacterClass(Component):
    NAME = 'character_class'
    __slots__ = ["base_classes"]

    def __init__(self, *base_classes):
        super().__init__()
        self.base_classes = base_classes

    def contains(self, base_class):
        if base_class in self.base_classes:
            return True

    def get_attack_bonus(self, level):
        best_attack_bonus = 0
        for base_class in self.base_classes:
            current_attack_bonus = base_class.level_table.get(level).attack_bonus
            if current_attack_bonus > best_attack_bonus:
                best_attack_bonus = current_attack_bonus

        return best_attack_bonus

    def get_hit_dice(self, level):
        levels = (base_class.level_table.get(level) for base_class in self.base_classes)
        hit_dices = [level.hit_dice for level in levels if level] if levels else None
        if not hit_dices:
            return None

        largest_hit_dice = max(hit_dices, key=lambda h: h.sides)
        restrictions = self.host.restrictions
        if restrictions and restrictions.hit_dice_max_size:
            restricted_dice = restrictions.hit_dice_max_size.dice
            if restricted_dice and largest_hit_dice > restricted_dice:
                largest_hit_dice = restricted_dice

        return largest_hit_dice

    def copy(self):
        return CharacterClass(
            type(*self.base_classes)()
        )
