from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.items.weapons.types import get_melee_weapon_types
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class MeleeWeaponRecipe(Recipe):
    name = "Base Melee Weapon Recipe"
    base_object_type = MeleeWeapon
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Melee(
                melee_damage=item_type.melee_damage,
                weapon_type=get_melee_weapon_types(item_type),
            )
        ]

        return new_components
