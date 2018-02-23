from bflib import dice
from bflib.characters.specialabilities import Hide as HideAbility
from core import effects
from core.abilities.base import Ability
from services import echo


class Hide(Ability):
    name = "Hide"
    target_selection = None

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if character.query.special_ability(HideAbility) <= 0:
            return False

        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        hide_target = character.query.special_ability(HideAbility)
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
            character.effects.add_effect(effects.Hidden(None))

        return True
