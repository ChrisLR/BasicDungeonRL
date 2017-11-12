from core.actions.base import Action
from services import echo
from services.selection import DirectionalSelection


class Open(Action):
    target_selection_types = DirectionalSelection,

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
            if target.openable and target.openable.closed:
                target.openable.open()
                if echo.functions.is_player(character):
                    echo.echo_service.echo("You open {}".format(target.name))
                else:
                    echo.echo_service.echo("{} opens {}".format(character.name, target.name))
                return True

        return False
