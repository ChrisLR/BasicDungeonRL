from bflib.items.ammunition.base import Ammunition
from bfgame import components
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class AmmunitionRecipe(Recipe):
    name = "Base Ammunition Recipe"
    base_object_type = Ammunition
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Ammunition(item_type.ammunition_type, item_type.ammunition_damage)
        ]

        return new_components
