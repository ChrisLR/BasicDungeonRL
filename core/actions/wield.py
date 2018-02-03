from core.actions.base import Action
from services import selection
from services.selection import filters


class Wield(Action):
    target_selection = selection.TargetSelectionSet(
        selections=selection.Inventory,
        filters=filters.ListBased,
    )

    @classmethod
    def can_execute(cls, character, selection=None):
        if not character.equipment:
            return False

        if not selection:
            return False
        return True

    @classmethod
    def execute(cls, character, selection=None):
        for target in selection:
            if not character.equipment.wield(target):
                return False
            else:
                character.inventory.remove(target)

        return True
