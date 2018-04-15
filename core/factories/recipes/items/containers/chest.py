from bflib.items import Chest
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


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
            components.Lock(False)
        ]

        return new_components
