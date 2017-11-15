from bflib.items.ammunition.base import Ammunition
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class AmmunitionRecipe(Recipe):
    name = "Base Ammunition Recipe"
    base_object_type = Ammunition
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type):
        new_components = [
            components.Ammunition(item_type.ammunition_type, item_type.ammunition_damage)
        ]

        return new_components
