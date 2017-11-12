import abc
from functools import total_ordering


@total_ordering
class AbilityScore(object):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["value"]

    _modifier_table = {
        1: -5,
        2: -4,
        3: -3,
        4: -2,
        5: -2,
        6: -1,
        7: -1,
        8: -1,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 1,
        14: 1,
        15: 1,
        16: 2,
        17: 2,
        18: 3,
        19: 3,
        20: 4,
        21: 4,
        22: 5,
        23: 5,
        24: 6,
        25: 6,
        26: 7,
        27: 7,
        28: 8,
        29: 9,
        30: 10,
    }

    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self.value

    def modifier(self, modifiers=0):
        return self._modifier_table[self.value + modifiers]

    def __eq__(self, other):
        return int(self) == int(other)

    def __lt__(self, other):
        return int(self) < int(other)


class Strength(AbilityScore):
    pass


class Dexterity(AbilityScore):
    pass


class Constitution(AbilityScore):
    pass


class Intelligence(AbilityScore):
    pass


class Wisdom(AbilityScore):
    pass


class Charisma(AbilityScore):
    pass
