class SavingThrow(object):
    __slots__ = ["value"]
    name = ""

    def __init__(self, value):
        self.value = value


class DeathPoison(SavingThrow):
    name = "Death/Poison"


class DragonBreath(SavingThrow):
    name = "Dragon Breath"


class ParalysisStone(SavingThrow):
    name = "Paralysis/Stone"


class Spells(SavingThrow):
    name = "Spells"


class Wands(SavingThrow):
    name = "Wands"
