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
        cls(
            ability_score=cls._merge_if_true(first.ability_score, other.ability_score),
            armor=cls._merge_if_true(first.armor, other.armor),
            classes=cls._merge_if_true(first.classes, other.classes),
            hit_dice_max_size=cls._merge_if_true(first.hit_dice_max_size, other.hit_dice_max_size),
            weapons=cls._merge_if_true(first.weapons, other.weapons),
            weapon_size=cls._merge_if_true(first.weapon_size, other.weapon_size),
        )

    @staticmethod
    def _merge_if_true(set_1, set_2):
        if set_1 and set_2:
            return type(set_1).from_merge(set_2)
        elif set_1 and not set_2:
            return set_1
        elif set_2 and not set_1:
            return set_2
        else:
            return None
