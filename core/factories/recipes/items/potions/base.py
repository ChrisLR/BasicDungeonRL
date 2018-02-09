from bflib.items.potions.base import Potion
from core import components, effects
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class PotionRecipe(Recipe):
    name = "Base Potion Recipe"
    base_object_type = Potion
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type):
        effect_type = next((effect for effect in effects.listing if effect.name == item_type.effect.name))
        effect = effect_type(item_type.effect.duration, dice=item_type.effect.dice)
        new_components = [
            components.Consumable(effect)
        ]

        return new_components
