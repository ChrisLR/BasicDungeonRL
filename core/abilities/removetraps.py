from bflib import dice
from bflib.characters.specialabilities import RemoveTraps as RemoveTrapsAbility
from core import components
from core.abilities.base import Ability
from services import echo
from services.selection import DirectionalSelection, filters, TargetSelectionSet


class RemoveTraps(Ability):
    name = "Remove Traps"
    target_selection = TargetSelectionSet(
        selections=DirectionalSelection,
        filters=filters.SingleListBased)

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        if target_selection[0].trap:
            if target_selection[0].trap.has_failed(character):
                echo.player_echo(
                    character, "You think there is no trap.")
                return False

        if character.query.special_ability(RemoveTrapsAbility) <= 0:
            return False

        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        remove_trap_target = character.query.special_ability(RemoveTrapsAbility)
        item = target_selection[0]
        value = dice.D100(1).roll()
        if not target_selection[0].trap or value > remove_trap_target:
            return echo.player_echo(character, "You think there is no trap.")
        else:
            echo.player_echo(
                character, "You found a " + item.trap.name)

        value = dice.D100(1).roll()
        echo.see(
            actor=character,
            actor_message="You attempt to disarm {}'s trap..."
                          "".format(item.name),
            observer_message="{} attempts to disarm {}'s trap..."
                             "".format(character.name, item.name)
        )
        if value > remove_trap_target:
            item.trap.add_failed_attempt(character, character.experience.level)
            return False
        else:
            item.unregister_component_name(components.Trap.NAME)

        return True
