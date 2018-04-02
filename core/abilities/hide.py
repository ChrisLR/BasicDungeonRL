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
        for game_object in character.location.level.game_objects:
            if game_object is character:
                continue

            if game_object.vision and game_object.vision.can_see_object(character):
                echo.player_echo(character, "You may not hide in plain sight.")
                return False

        hide_target = character.query.special_ability(HideAbility)
        value = dice.D100(1).roll()
        if value > hide_target:
            if character.effects.has_effect(effects.Hidden):
                character.effects.remove_effect(effects.Hidden)

            echo.see(
                actor=character,
                actor_message="You attempt to hide.",
                observer_message="{} unsuccessfully attempts to hide."
                                 "".format(character.name)
            )
            return False
        else:
            echo.player_echo(character, "You attempt to hide.")
            if not character.effects.has_effect(effects.Hidden):
                character.effects.add_effect(effects.Hidden(None))

        return True
