from core.actions.base import Action
from services.selection import DirectionalSelection, filters


class Get(Action):
    target_selection_types = DirectionalSelection,
    target_filters = (
        filters.TileExclusion,
        filters.Conscious,
        filters.Hierarchy,
    )

    @classmethod
    def can_execute(cls, character, selection=None):
        if not character.equipment and not character.inventory:
            return False

        if not selection:
            return False
        return True

    @classmethod
    def execute(cls, character, selection=None):
        if not selection:
            return False

        for target in selection:
            if not character.inventory.add(target):
                if not character.equipment.wield(target):
                    return False

            target_level = target.location.level
            if target_level:
                target_level.remove_object(target)

        return True
