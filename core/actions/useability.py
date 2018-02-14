from core.actions.base import Action
from services import echo, selection
from services.selection import filters
from core.game.manager import game


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
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        if not target_selection:
            return False

        return game.game_context.action_stack.add_action_to_stack(target_selection[0])
