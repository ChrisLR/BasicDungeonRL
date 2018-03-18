from core.actions.base import Action
from services.selection import CursorSelection, TargetSelectionSet


class Look(Action):
    id = "look"
    target_selection = TargetSelectionSet(CursorSelection)

    @classmethod
    def can_execute(cls, character, target_selection=None):
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        return True
