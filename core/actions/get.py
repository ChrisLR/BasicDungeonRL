from core.actions.base import Action
from services.selection import DirectionalSelection, filters
from services.selection.base import TargetSelectionSet


class Get(Action):
    name = "get"
    target_selection = TargetSelectionSet(
        selections=DirectionalSelection,
        filters=(
            filters.TileExclusion,
            filters.Conscious,
            filters.Hierarchy
        )
    )

    def can_execute(self, character, target_selection=None):
        if not character.equipment and not character.inventory:
            return False

        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        if not target_selection:
            return False

        for target in target_selection:
            if not self.added_worn_wielded(character, target):
                return False

            target_level = target.location.level
            if target_level:
                target_level.remove_object(target)

        return True

    def added_worn_wielded(self, character, target):
        if (not character.inventory.add(target)
                and not character.equipment.wear(target)
                and not character.equipment.wield(target)):
            return False
        return True
