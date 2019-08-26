from bflib import dice
from bflib.characters.specialabilities import MoveSilently as MoveSilentlyAbility
from bfgame.abilities.base import Ability


class MoveSilently(Ability):
    name = "Move Silently"
    requires = {MoveSilentlyAbility}
    target_selection = None
    use_manually = False

    def can_execute(self, character, target_selection=None):
        if character.query.special_ability(MoveSilentlyAbility) <= 0:
            return False

        return True

    def execute(self, character, target_selection=None):
        hide_target = character.query.special_ability(MoveSilentlyAbility)
        value = dice.D100(1).roll_total()
        if value > hide_target:
            self.game.echo.player(character, "You fail to move silently.")
            return False
        return True
