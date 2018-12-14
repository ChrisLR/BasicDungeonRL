from bfgame.actions.base import Action


class Bump(Action):
    name = "bump"

    def execute(self, character, target_selection=None):
        target = target_selection[0]
        if character.combat and target.combat:
            # TODO Then if it is an ally
            # TODO Then we start an attack.
            if character.ai and target not in character.ai.short_term_state.enemies:
                return

            self.game.attacks.auto_attack(character, target)

        return False
