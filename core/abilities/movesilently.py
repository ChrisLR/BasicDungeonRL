from bflib import dice
from bflib.characters.specialabilities import MoveSilently as MoveSilentlyAbility
from core.abilities.base import Ability


class MoveSilently(Ability):
    name = "Hide"
    target_selection = None

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if character.query.special_ability(MoveSilentlyAbility) <= 0:
            return False

        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        hide_target = character.query.special_ability(MoveSilentlyAbility)
        value = dice.D100(1).roll()
        if value > hide_target:
            return False
        return True
