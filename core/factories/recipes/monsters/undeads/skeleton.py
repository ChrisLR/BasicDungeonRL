from bflib import monsters
from core import components
from core.ai import personalities
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.monsters.undeads.base import UndeadRecipe
from core.outfits.monsters import skeletons as skeleton_outfits


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
        ]

        return new_components
