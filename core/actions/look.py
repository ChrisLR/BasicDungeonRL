from core.actions.base import Action
from services.selection import CursorSelection, TargetSelectionSet


class Look(Action):
    target_selection = TargetSelectionSet(CursorSelection)

    @classmethod
    def can_execute(cls, character, selection=None):
        return True

    @classmethod
    def execute(cls, character, selection=None):
        return True
