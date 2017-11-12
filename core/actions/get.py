from core.actions.base import Action
from services.selection import DirectionalSelection, filters


class Get(Action):
    target_selection_types = DirectionalSelection,
    target_filters = filters.TileExclusionFilter, filters.ListBasedSelectionFilter,

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
            target.location.level.remove_object(target)

        return True
