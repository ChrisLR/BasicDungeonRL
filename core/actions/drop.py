from core import contexts
from core.actions.base import Action
from core.messaging import StringBuilder, Verb, Actor, Target
from services.selection import AllItems, filters, TargetSelectionSet


class Drop(Action):
    name = "drop"
    target_selection = TargetSelectionSet(
        selections=AllItems,
        filters=filters.ListBased,
    )

    def can_execute(self, character, target_selection=None):
        if not character.equipment:
            return False

        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        level = character.location.level
        for target in target_selection:
            if character.inventory.remove(target) or character.equipment.remove(target):
                target.location.update_from_other(character.location)
                level.add_object(target)
                context = contexts.Action(character, target)
                message = StringBuilder(Actor, Verb("drop", Actor), Target)
                self.game.echo.see(character, message, context)

        return True
