from core.actions.base import Action
from services.selection import AllItems, filters, TargetSelectionSet


class Drop(Action):
    target_selection = TargetSelectionSet(
        selections=AllItems,
        filters=filters.ListBased,
    )

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not character.equipment:
            return False

        if not target_selection:
            return False
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        level = character.location.level
        for target in target_selection:
            if character.inventory.remove(target) or character.equipment.remove(target):
                target.location.update_from_other(character.location)
                level.add_object(target)

        return True
