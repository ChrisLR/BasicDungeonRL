from bflib import monsters
from bfgame import components
from core import bodies
from core.ai import personalities
from bfgame.factories.recipes import listing
from bfgame.factories.recipes.base import Recipe
from bfgame.factories.recipes.monsters.undeads.base import UndeadRecipe
from bfgame.outfits.monsters import skeletons as skeleton_outfits


# noinspection PyTypeChecker
@listing.register
class SkeletonRecipe(Recipe):
    name = "Skeleton Recipe"
    base_object_type = monsters.Skeleton
    depends_on = [UndeadRecipe]
    outfits = (skeleton_outfits.SkeletonPack1, skeleton_outfits.SkeletonPack2)

    @staticmethod
    def build_components(monster_type, game):
        new_components = [
            components.AI(personalities.MindlessBerserk),
            components.Body(bodies.HumanoidBody()),
            components.Equipment()
        ]

        return new_components
