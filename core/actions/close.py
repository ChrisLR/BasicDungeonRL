from core import contexts
from core.actions.base import Action
from core.actions.listing import register
from messaging import StringBuilder, Verb, Actor, Target
from services.selection import DirectionalSelection, TargetSelectionSet


@register
class Close(Action):
    id = "close"
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
