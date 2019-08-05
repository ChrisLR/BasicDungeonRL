from bflib import units
from bfgame.abilities.base import Ability
from bfgame.effects.burning import Burning
from services.selection import CursorSelection, TargetSelectionSet

"""
Yes for anyone wondering, its a joke, for debug.
"""


class Immolation(Ability):
    name = "Immolation"
    target_selection = TargetSelectionSet(CursorSelection)

    @classmethod
    def can_execute(cls, character, target_selection=None):
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        """
        Set yourself on fire! Whoosh!
        """
        for target in target_selection:
            effector = target.effects
            if effector:
                effector.add_effect(Burning(units.CombatRound(4)))


class SmallImmolation(Immolation):
    name = "SmallImmolation"

    @classmethod
    def execute(cls, character, target_selection=None):
        """
        Set yourself on fire, just a bit.
        """

        for target in target_selection:
            effector = target.effects
            if effector:
                effector.add_effect(Burning(units.CombatRound(0)))


class InfiniteImmolation(Immolation):
    name = "InfiniteImmolation"

    @classmethod
    def execute(cls, character, target_selection=None):
        """
        Set yourself on fire, FOR ETERNITY
        """
        for target in target_selection:
            effector = target.effects
            if effector:
                effector.add_effect(Burning(None))
