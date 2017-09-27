import abc
import random


class Dice(object):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["amount", "flat_bonus"]

    @abc.abstractclassmethod
    def sides(self):
        pass

    def __init__(self, amount, flat_bonus=0):
        self.amount = amount
        self.flat_bonus = flat_bonus

    def roll(self):
        return sum((random.randint(1, self.sides) for _ in range(0, self.amount))) + self.flat_bonus

    @classmethod
    def manual_roll(cls, amount, flat_bonus=0):
        return sum((random.randint(1, cls.sides) for _ in range(0, amount))) + flat_bonus

    @staticmethod
    def get_by_sides(sides):
        for dice in dice_listing:
            if dice.sides == sides:
                return dice


class D1(Dice):
    sides = 1


class D2(Dice):
    sides = 1


class D4(Dice):
    sides = 4


class D6(Dice):
    sides = 6


class D8(Dice):
    sides = 8


class D10(Dice):
    sides = 10


class D12(Dice):
    sides = 12


class D20(Dice):
    sides = 20


class D100(Dice):
    sides = 100

dice_listing = (
    D1,
    D2,
    D4,
    D6,
    D8,
    D10,
    D12,
    D20,
    D100,
)