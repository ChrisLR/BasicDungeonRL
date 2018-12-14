from bflib import dice
from bflib.characters.specialabilities import RemoveTraps as RemoveTrapsAbility
from bfgame import components, contexts
from bfgame.abilities.base import Ability
from services.selection import DirectionalSelection, filters, TargetSelectionSet
from messaging import StringBuilder, Actor, Verb, Target


class RemoveTraps(Ability):
    name = "Remove Traps"
    target_selection = TargetSelectionSet(
        selections=DirectionalSelection,
        filters=filters.SingleListBased)

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False

        if target_selection[0].trap:
            if target_selection[0].trap.has_failed(character):
                self.game.echo.player(character, "You think there is no trap.")
                return False

        if character.query.special_ability(RemoveTrapsAbility) <= 0:
            return False

        return True

    def execute(self, character, target_selection=None):
        remove_trap_target = character.query.special_ability(RemoveTrapsAbility)
        item = target_selection[0]
        value = dice.D100(1).roll_total()
        context = contexts.Action(character, item)
        if not target_selection[0].trap or value > remove_trap_target:
            self.game.echo.player(character, "You think there is no trap.")
            return False
        else:
            message = StringBuilder(Actor, Verb("found", Actor), "a", Target)
            self.game.player(character, message, context)

        value = dice.D100(1).roll_total()
        message = StringBuilder(Actor, Verb("attempt", Actor), "to disarm", Target, "'s trap...")
        self.game.see(character, message, context)
        if value > remove_trap_target:
            item.trap.add_failed_attempt(character, character.experience.level)
            return False
        else:
            item.unregister_component_name(components.Trap.NAME)

        return True
