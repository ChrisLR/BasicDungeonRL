from core.actions.base import Action
from services import echo
from services.selection import DirectionalSelection, TargetSelectionSet


class Close(Action):
    target_selection = TargetSelectionSet(DirectionalSelection)

    @classmethod
    def can_execute(cls, character, selection=None):
        if not selection:
            return False
        return True

    @classmethod
    def execute(cls, character, selection=None):
        if not selection:
            return False

        for target in selection:
            if target.openable and not target.openable.closed:
                target.openable.close()
                if echo.functions.is_player(character):
                    echo.echo_service.echo(
                        "You close {}".format(target.name))
                else:
                    echo.echo_service.echo(
                        "{} closes {}".format(character.name, target.name))

                return True

        return False
