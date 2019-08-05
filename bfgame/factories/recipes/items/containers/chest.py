from bfgame import components as bf_components
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe
from bflib.items import Chest
from core import components


# noinspection PyTypeChecker
@listing.register
class ChestRecipe(Recipe):
    name = "Chest Recipe"
    base_object_type = Chest
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Container(
                container_type=item_type.container_type,
                volume_limit=item_type.volume_limit,
                weight_limit=item_type.weight_limit
            ),
            components.Openable(),
            bf_components.Lock(False)
        ]

        return new_components
