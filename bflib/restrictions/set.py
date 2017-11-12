from bflib.util import merge_set_if_true


class RestrictionSet(object):
    __slots__ = ["ability_score", "armor", "classes", "hit_dice_max_size", "weapons", "weapon_size"]

    def __init__(self, ability_score=None, armor=None, classes=None, hit_dice_max_size=None,
                 weapons=None, weapon_size=None):
        self.ability_score = ability_score
        self.armor = armor
        self.classes = classes
        self.hit_dice_max_size = hit_dice_max_size
        self.weapons = weapons
        self.weapon_size = weapon_size

    @classmethod
    def from_merge(cls, first, other):
        return cls(
            ability_score=merge_set_if_true(first.ability_score, other.ability_score),
            armor=merge_set_if_true(first.armor, other.armor),
            classes=merge_set_if_true(first.classes, other.classes),
            hit_dice_max_size=merge_set_if_true(first.hit_dice_max_size, other.hit_dice_max_size),
            weapons=merge_set_if_true(first.weapons, other.weapons),
            weapon_size=merge_set_if_true(first.weapon_size, other.weapon_size),
        )
