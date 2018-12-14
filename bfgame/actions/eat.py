from bfgame import components, contexts
from bfgame.actions.base import Action
from messaging import StringBuilder, Verb, Actor, Target
from services.selection import AllItems, filters, TargetSelectionSet


class ConsumableFilter(filters.Component):
    component = components.Consumable


class Eat(Action):
    name = "eat"
    target_selection = TargetSelectionSet(
        selections=AllItems,
        filters=(ConsumableFilter, filters.SingleListBased),
    )

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False
        return True

    def execute(self, character, target_selection=None):
        target = target_selection[0]
        effects = target.consumable.effects
        for effect in effects:
            character.effects.add_effect(effect)

        if not character.inventory.remove(target):
            character.equipment.remove(target)

        context = contexts.Action(character, target)
        message = StringBuilder(Actor, Verb("eat", Actor), Target)
        self.game.echo.see(character, message, context)

        return True
