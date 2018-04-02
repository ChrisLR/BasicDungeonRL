from core.actions.base import Action
from services.selection import EquippedSelection, filters, TargetSelectionSet


class Remove(Action):
    name = "remove"
    target_selection = TargetSelectionSet(
        selections=EquippedSelection,
        filters=filters.ListBased
    )

    def can_execute(self, character, target_selection=None):
        if not character.equipment:
            return False

        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        level = character.location.level
        for target in target_selection:
            if not character.equipment.remove(target):
                return False
            else:
                if not character.inventory.add(target):
                    target.location.update_from_other(character.location)
                    level.add_object(target)

        return True
