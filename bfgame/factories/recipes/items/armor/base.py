from bflib.items.armor.base import Armor
from bfgame import components
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class ArmorRecipe(Recipe):
    name = "Base Armor Recipe"
    base_object_type = Armor
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Armor(
                item_type.armor_class,
                item_type.armor_type
            )
        ]

        return new_components
