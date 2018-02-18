from core.actions.base import Action
from core import events
from services import echo
from services.selection import DirectionalSelection, TargetSelectionSet


class Open(Action):
    target_selection = TargetSelectionSet(DirectionalSelection)

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        for target in target_selection:
            if target.openable and target.openable.closed:
                if target.openable.open():
                    echo.see(
                        actor=character,
                        actor_message="You open {}".format(target.name),
                        observer_message="{} opens {}".format(
                            character.name, target.name),
                    )
                    if target.events:
                        target.events.transmit(events.Opened(character))

                    return True
                else:
                    echo.player_echo(
                        actor=character,
                        message="The {} is locked!".format(target.name)
                    )

        return False
