from core.actions.base import Action
from services.selection import DirectionalSelection


class Open(Action):
    target_selection_type = DirectionalSelection

    @classmethod
    def can_execute(cls, character, selection=None):
        if not selection:
            return False
        return True

    @classmethod
    def execute(cls, character, selection=None):
        if not selection:
            return False

        for target in selection.targets:
            if target.openable and target.openable.closed:
                target.openable.open()
                return True

        return False
