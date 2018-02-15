import abc


class Attack(object):
    name = ""
    __metaclass__ = abc.ABCMeta

    def __init__(self, damage_dice, damage_bonus=0):
        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus


class WeaponAttack(Attack):
    name = "Weapon"


class NaturalAttack(Attack):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["damage_dice", "damage_bonus"]
    name = ""
