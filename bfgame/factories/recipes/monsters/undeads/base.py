from bflib.keywords.items import WearLocation, WieldLocation
from bflib.monsters.undeads.base import Undead
from bfgame import components
from bfgame.factories.recipes import listing, Recipe
from bfgame.factories.recipes.monsters import MonsterRecipe


@listing.register
class UndeadRecipe(Recipe):
    name = "Undead Recipe"
    base_object_type = Undead
    depends_on = [MonsterRecipe]
    outfits = None

    @staticmethod
    def build_components(monster_type, game):
        # TODO This method of assigning wear locations is bad.
        new_components = []

        return new_components
