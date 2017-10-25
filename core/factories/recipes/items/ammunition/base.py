from bflib.items.ammunition.base import Ammunition
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class AmmunitionRecipe(Recipe):
    name = "Base Ammunition Recipe"
    base_item_type = Ammunition
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.Ammunition(cls.base_item_type.ammunition_type, cls.base_item_type.ammunition_damage)
        ]

        return new_components
