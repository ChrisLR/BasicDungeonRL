from bflib import units
from core.abilities.base import Ability
from core.effects.burning import Burning


"""
Yes for anyone wondering, its a joke, for debug.
"""


class Immolation(Ability):
    name = "Immolation"

    @classmethod
    def can_execute(cls, game_object):
        return True

    @classmethod
    def execute(cls, game_object):
        """
        Set yourself on fire! Whoosh!
        """
        game_object.effects.add_effect(Burning(units.CombatRound(4)))


class SmallImmolation(Ability):
    name = "SmallImmolation"

    @classmethod
    def can_execute(cls, game_object):
        return True

    @classmethod
    def execute(cls, game_object):
        """
        Set yourself on fire, just a bit.
        """
        game_object.effects.add_effect(Burning(units.CombatRound(0)))


class InfiniteImmolation(Ability):
    name = "InfiniteImmolation"

    @classmethod
    def can_execute(cls, game_object):
        return True

    @classmethod
    def execute(cls, game_object):
        """
        Set yourself on fire, FOR ETERNITY
        """
        game_object.effects.add_effect(Burning(None))
