from core.actions.base import Action
from services import echo
from services.selection import DirectionalSelection, TargetSelectionSet


class Close(Action):
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
            if target.openable and not target.openable.closed:
                target.openable.close()
                echo.see(
                    actor=character,
                    actor_message="You close {}".format(target.name),
                    observer_message="{} closes {}".format(
                        character.name, target.name
                    ),
                )

                return True

        return False
