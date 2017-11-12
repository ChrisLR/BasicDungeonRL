from core.actions.base import Action
from services.selection import DirectionalSelection, filters
from services import echo


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


class Close(Action):
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
            if target.openable and not target.openable.closed:
                target.openable.close()
                if echo.functions.is_player(character):
                    echo.echo_service.echo("You close {}".format(target.name))
                else:
                    echo.echo_service.echo("{} closes {}".format(character.name, target.name))

                return True

        return False


class Get(Action):
    target_selection_types = DirectionalSelection,
    target_filters = filters.ListBasedSelectionFilter,

    @classmethod
    def can_execute(cls, character, selection=None):
        if not character.equipment and not character.inventory:
            return False

        if not selection:
            return False
        return True

    @classmethod
    def execute(cls, character, selection=None):
        if not selection:
            return False

        for target in selection:
            if not character.inventory.add(target):
                if not character.equipment.wield(target):
                    return False
            target.location.level.remove_object(target)

        return True
