from core.actions.base import Action
from core.actions.listing import register


@register
class Bump(Action):
    id = "bump"

    def execute(self, character, target_selection=None):
        target = target_selection[0]
        if character.combat and target.combat:
            # TODO Then if it is an ally
            # TODO Then we start an attack.
            if character.ai and target not in character.ai.short_term_state.enemies:
                return

            self.game.attack.auto_attack(character, target)

        return False
