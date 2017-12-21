from bflib import monsters
from core import components
from core.ai import personalities
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.monsters.humanoids.base import HumanoidRecipe
from core.outfits.monsters import goblins as goblin_outfits


# noinspection PyTypeChecker
@listing.register
class GoblinRecipe(Recipe):
    name = "Goblin Recipe"
    base_object_type = monsters.Goblin
    depends_on = [HumanoidRecipe]
    outfits = (goblin_outfits.GoblinPack1, goblin_outfits.GoblinPack2)

    @staticmethod
    def build_components(monster_type):
        new_components = [
            components.AI(personalities.Goblin),
        ]

        return new_components
