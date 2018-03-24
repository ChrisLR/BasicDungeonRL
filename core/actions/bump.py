from core.actions.base import Action
from core.actions.listing import register


@register
class Bump(Action):
    id = "bump"

    @classmethod
    def execute(cls, character, target):
        if character.combat and target.combat:
            # TODO Then if it is an ally
            # TODO Then we start an attack.
            if character.ai and target not in character.ai.short_term_state.enemies:
                return

            # TODO This should instead use its own "game"
            character.game.attack.auto_attack(character, target)

        return False
