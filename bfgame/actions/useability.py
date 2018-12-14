from bfgame.actions.base import Action
from services import selection
from services.selection import filters


class UseAbility(Action):
    name = "use_ability"
    target_selection = selection.TargetSelectionSet(
        selections=selection.UsableAbilities,
        filters=filters.SingleListBased
    )

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        if not target_selection:
            return False

        return self.game.action_stack.add_action_to_stack(target_selection[0])
