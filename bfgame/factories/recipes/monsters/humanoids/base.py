from bfgame import components as bf_components
from bfgame.factories.recipes import listing, Recipe
from bfgame.factories.recipes.monsters import MonsterRecipe
from bflib.monsters.humanoids.base import Humanoid
from core import bodies, components


@listing.register
class HumanoidRecipe(Recipe):
    name = "Humanoid Recipe"
    base_object_type = Humanoid
    depends_on = [MonsterRecipe]
    outfits = None

    @staticmethod
    def build_components(monster_type, game):
        # TODO This method of assigning wear locations is bad.
        new_components = [
            bf_components.Equipment(),
            components.Body(bodies.HumanoidBody())
        ]

        return new_components
