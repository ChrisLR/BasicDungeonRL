from bflib.items.armor.base import Armor
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class ArmorRecipe(Recipe):
    name = "Base Armor Recipe"
    base_item_type = Armor
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.Armor(
                cls.base_item_type.armor_class,
                cls.base_item_type.armor_type
            )
        ]

        return new_components
