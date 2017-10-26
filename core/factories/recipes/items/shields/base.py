from bflib.items.shields.base import Shield
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class ShieldRecipe(Recipe):
    name = "Base Shield Recipe"
    base_item_type = Shield
    depends_on = [ItemRecipe]

    @classmethod
    def build_components(cls):
        new_components = [
            components.Shield(
                armor_class_melee=cls.base_item_type.armor_class_melee,
                armor_class_missile=cls.base_item_type.armor_class_missile,
            )
        ]

        return new_components
