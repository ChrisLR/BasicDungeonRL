from core.actions.base import Action
from services import selection
from services.selection import filters


# TODO This wont work as is because of target selection.
# TODO Abilities Should be treated like an action themselves.
class UseAbility(Action):
    name = "use_ability"
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
