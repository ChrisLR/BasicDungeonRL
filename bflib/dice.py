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
