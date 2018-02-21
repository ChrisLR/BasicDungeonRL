from bflib import dice
from bflib.characters.specialabilities import Hide as HideAbility
from core import components
from core.abilities.base import Ability
from services import echo
from services.selection import DirectionalSelection, filters, TargetSelectionSet


class Hide(Ability):
    name = "Hide"
    target_selection = None

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        if character.query.special_ability(HideAbility) <= 0:
            return False

        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        hide_target = character.query.special_ability(HideAbility)
        item = target_selection[0]
        value = dice.D100(1).roll()
        # TODO Actual Mechanic to keep a STEALTHED value or effect, so others dont see.
        if value > hide_target:
            echo.see(
                actor=character,
                actor_message="You attempt to hide.",
                observer_message="{} unsuccessfully attempts to hide."
                                 "".format(character.name)
            )
            return False
        else:
            echo.player_echo(character, "You attempt to hide.")

        return True
