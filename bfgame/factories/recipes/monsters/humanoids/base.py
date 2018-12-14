from bflib.keywords.items import WearLocation, WieldLocation
from bflib.monsters.humanoids.base import Humanoid

from bfgame import bodies, components
from bfgame.factories.recipes import listing, Recipe
from bfgame.factories.recipes.monsters import MonsterRecipe


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
            components.Equipment(),
            components.Body(bodies.HumanoidBody())
        ]

        return new_components
