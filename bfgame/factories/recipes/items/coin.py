from bflib.items.coins import Coin
from bfgame import components
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class CoinRecipe(Recipe):
    name = "Coin Recipe"
    base_object_type = Coin
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        name = item_type.name if item_type.name else item_type.__name__

        # This is weird, I know, but a coin is both a price and an item.
        new_components = [
            components.Valuable(item_type)
        ]

        return new_components
