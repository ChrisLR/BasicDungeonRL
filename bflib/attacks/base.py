import abc


class Attack(object):
    name = ""
    __slots__ = ["damage_dice", "attack_bonus", "damage_bonus"]
    __metaclass__ = abc.ABCMeta

    def __init__(self, damage_dice,  attack_bonus=0, damage_bonus=0):
        self.attack_bonus = attack_bonus
        self.damage_dice = damage_dice
        self.damage_bonus = damage_bonus


class WeaponAttack(Attack):
    name = "Weapon"


class NaturalAttack(Attack):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["damage_dice", "damage_bonus"]
    name = ""
