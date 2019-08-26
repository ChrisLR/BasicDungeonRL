from bfgame import effects
from bfgame.abilities.base import Ability
from bflib import dice
from bflib.characters.specialabilities import Hide as HideAbility
from core import contexts
from core.messaging import StringBuilder, Actor, Verb


class Hide(Ability):
    name = "Hide"
    requires = {HideAbility}
    target_selection = None

    def can_execute(self, character, target_selection=None):
        if character.query.special_ability(HideAbility) <= 0:
            return False

        return True

    def execute(self, character, target_selection=None):
        for game_object in character.location.level.game_objects:
            if game_object is character:
                continue

            if game_object.vision and game_object.vision.can_see_object(character):
                self.game.echo.player(character, "You may not hide in plain sight.")
                return False

        hide_target = character.query.special_ability(HideAbility)
        value = dice.D100(1).roll_total()
        if value > hide_target:
            if character.effects.has_effect(effects.Hidden):
                character.effects.remove_effect(effects.Hidden)

            context = contexts.Action(character, None)
            self.game.echo.see(
                actor=character,
                message=StringBuilder(Actor, Verb("fail", Actor),  "to hide."),
                context=context
            )
            return False
        else:
            self.game.echo.player(character, "You manage to hide.")
            if not character.effects.has_effect(effects.Hidden):
                character.effects.add_effect(effects.Hidden(None))

        return True
