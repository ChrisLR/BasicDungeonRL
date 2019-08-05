from bfgame import effects
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe
from bflib.items.potions.base import Potion
from core import components


# noinspection PyTypeChecker
@listing.register
class PotionRecipe(Recipe):
    name = "Base Potion Recipe"
    base_object_type = Potion
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        effect_type = next((effect for effect in effects.listing if effect.name == item_type.effect.name))
        effect = effect_type(item_type.effect.duration, dice=item_type.effect.dice)
        new_components = [
            components.Consumable(effect)
        ]

        return new_components
