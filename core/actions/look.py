from core.actions.base import Action
from services.selection import CursorSelection, TargetSelectionSet


class Look(Action):
    name = "look"
    target_selection = TargetSelectionSet(CursorSelection)

    def can_execute(self, character, target_selection=None):
        return True

    def execute(self, character, target_selection=None):
        return True
