from bfgame.ai import personalities
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.monsters.base import MonsterRecipe
from bflib import monsters
from core import components


# noinspection PyTypeChecker
@listing.register
class ArachnidRecipe(Recipe):
    name = "Arachnid Recipe"
    base_object_type = monsters.GiantBlackWidow
    depends_on = [MonsterRecipe]
    outfits = None

    @staticmethod
    def build_components(monster_type, game):
        new_components = [
            components.AI(personalities.Goblin),
        ]

        return new_components
