from core.actions.base import Action
from core import contexts
from core import events
from services.selection import DirectionalSelection, TargetSelectionSet
from core.messaging import StringBuilder, Verb, Actor, Target


class Open(Action):
    name = "open"
    target_selection = TargetSelectionSet(DirectionalSelection)

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        if not target_selection:
            return False

        for target in target_selection:
            if target.openable and target.openable.closed:
                if target.openable.open():
                    context = contexts.Action(character, target)
                    message = StringBuilder(Actor, Verb("open", Actor), Target)
                    self.game.echo.see(character, message, context)
                    if target.events:
                        target.events.transmit(events.Opened(character))

                    return True
                else:
                    context = contexts.Action(character, target)
                    message = StringBuilder(Actor, Verb("try", Actor), "to open", Target, "but it is locked!")
                    self.game.echo.see(character, message, context)

        return False
