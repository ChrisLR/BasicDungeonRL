from core.actions.base import Action
from core import components
from services.selection import AllItems, filters, TargetSelectionSet


class ConsumableFilter(filters.Component):
    component = components.Consumable


class Eat(Action):
    target_selection = TargetSelectionSet(
        selections=AllItems,
        filters=(ConsumableFilter, filters.SingleListBased),
    )

    @classmethod
    def can_execute(cls, character, target_selection=None):
        if not target_selection:
            return False
        return True

    @classmethod
    def execute(cls, character, target_selection=None):
        effects = target_selection[0].consumable.effects
        for effect in effects:
            character.effects.add_effect(effect)

        if not character.inventory.remove(target_selection[0]):
            character.equipment.remove(target_selection[0])

        return True
