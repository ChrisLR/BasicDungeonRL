from core import components
from core.actions.base import Action
from services import selection
from services.selection import filters


# noinspection PyAbstractClass
class WearableFilter(filters.Component):
    component = components.Wearable


class Wear(Action):
    name = "wear"
    target_selection = selection.TargetSelectionSet(
        selections=(selection.Inventory, selection.Wielded),
        filters=(WearableFilter, filters.ListBased),
    )

    def can_execute(self, character, target_selection=None):
        if not character.equipment:
            return False

        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        for target in target_selection:
            if target in character.equipment.wielded_items():
                character.equipment.remove(target)

            if not character.equipment.wear(target):
                return False
            else:
                character.inventory.remove(target)

        return True
