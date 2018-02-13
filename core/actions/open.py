from core.actions.base import Action
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
                    if echo.functions.is_player(character):
                        echo.echo_service.echo(
                            "You open {}".format(target.name))
                    else:
                        echo.echo_service.echo(
                            "{} opens {}".format(character.name, target.name))
                    return True
                else:
                    if echo.functions.is_player(character):
                        echo.echo_service.echo(
                            "The {} is locked!".format(target.name))

        return False
