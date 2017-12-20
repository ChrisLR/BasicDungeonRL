from bflib import monsters
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
