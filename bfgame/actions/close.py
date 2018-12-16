from core import contexts
from bfgame.actions.base import Action
from core.messaging import StringBuilder, Verb, Actor, Target
from services.selection import DirectionalSelection, TargetSelectionSet


class Close(Action):
    name = "close"
    target_selection = TargetSelectionSet(DirectionalSelection)

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        if not target_selection:
            return False

        for target in target_selection:
            if target.openable and not target.openable.closed:
                target.openable.close()
                context = contexts.Action(character, target)
                message = StringBuilder(Actor, Verb("close", Actor), Target)
                self.game.echo.see(character, message, context)
                return True

        return False
