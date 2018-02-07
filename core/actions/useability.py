from core.actions.base import Action
from services import echo, selection
from services.selection import filters


# TODO This wont work as is because of target selection.
# TODO Abilities Should be treated like an action themselves.
class UseAbility(Action):
    target_selection = selection.TargetSelectionSet(
        selections=selection.UseableAbilities,
        filters=filters.SingleListBased
    )

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False
        return target_selection[0].can_execute(character)

    @classmethod
    def execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        return target_selection[0].execute(character)
