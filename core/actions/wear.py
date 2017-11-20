from core import components
from core.actions.base import Action
from services import selection as selection_service
from services.selection import filters


# noinspection PyAbstractClass
class WearableFilter(filters.ComponentFilter):
    component = components.Wearable


class Wear(Action):
    target_selection_types = selection_service.Inventory, selection_service.Wielded
    target_filters = WearableFilter, filters.ListBasedSelectionFilter

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
            if not character.equipment.wear(target):
                return False
            else:
                character.inventory.remove(target)

        return True
