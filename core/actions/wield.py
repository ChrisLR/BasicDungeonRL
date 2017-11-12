from core.actions.base import Action
from services.selection import InventorySelection


class Wield(Action):
    target_selection_types = InventorySelection,
    target_filters = None

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
