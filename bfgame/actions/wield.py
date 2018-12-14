from bfgame.actions.base import Action
from services import selection
from services.selection import filters


class Wield(Action):
    name = "wield"
    target_selection = selection.TargetSelectionSet(
        selections=selection.Inventory,
        filters=filters.ListBased,
    )

    def can_execute(self, character, target_selection=None):
        if not character.equipment:
            return False

        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        for target in target_selection:
            if not character.equipment.wield(target):
                return False
            else:
                character.inventory.remove(target)

        return True
