from bflib import monsters
from bfgame import components
from bfgame.ai import personalities
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.monsters.humanoids.base import HumanoidRecipe
from bfgame.outfits.monsters import goblins as goblin_outfits


# noinspection PyTypeChecker
@listing.register
class GoblinRecipe(Recipe):
    name = "Goblin Recipe"
    base_object_type = monsters.Goblin
    depends_on = [HumanoidRecipe]
    outfits = (goblin_outfits.GoblinPack1, goblin_outfits.GoblinPack2)

    @staticmethod
    def build_components(monster_type, game):
        new_components = [
            components.AI(personalities.Goblin),
        ]

        return new_components
