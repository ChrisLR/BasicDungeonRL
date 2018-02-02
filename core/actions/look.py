from core.actions.base import Action
from services.selection import CursorSelection


class Look(Action):
    target_selection_types = CursorSelection,

    @classmethod
    def can_execute(cls, character, selection=None):
        return True

    @classmethod
    def execute(cls, character, selection=None):
        return True
