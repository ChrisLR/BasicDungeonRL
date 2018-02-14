from collections import Iterable


class SpecialAbilitySet(object):
    __slots__ = ["special_abilities"]

    def __init__(self, special_abilities=None):
        self.special_abilities = special_abilities

    def __iter__(self):
        if isinstance(self.special_abilities, Iterable):
            for special_ability in self.special_abilities:
                yield special_ability
        else:
            yield self.special_abilities
            raise StopIteration
