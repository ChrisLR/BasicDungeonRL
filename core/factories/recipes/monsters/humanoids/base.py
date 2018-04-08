from bflib.keywords.items import WearLocation, WieldLocation
from bflib.monsters.humanoids.base import Humanoid

from core import bodies, components
from core.factories.recipes import listing, Recipe
from core.factories.recipes.monsters import MonsterRecipe


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
            components.Equipment(
                wear_locations=[
                    WearLocation.Head,
                    WearLocation.Torso,
                    WearLocation.Arms,
                    WearLocation.Hands,
                    WearLocation.Legs,
                    WearLocation.Feet,
                ],
                wield_locations=[
                    WieldLocation.LeftHand,
                    WieldLocation.RightHand
                ]
            ),
            components.Body(bodies.HumanoidBody(game))
        ]

        return new_components
