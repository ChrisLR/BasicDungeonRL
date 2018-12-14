from bflib.items.shields.base import Shield
from bfgame import components
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class ShieldRecipe(Recipe):
    name = "Base Shield Recipe"
    base_object_type = Shield
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Shield(
                armor_class_melee=item_type.armor_class_melee,
                armor_class_missile=item_type.armor_class_missile,
            )
        ]

        return new_components
