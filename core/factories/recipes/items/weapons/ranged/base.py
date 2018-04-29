from bflib.items.weapons.ranged.base import RangedWeapon
from bflib.items.weapons.types import get_melee_weapon_types
from core import components
from core.factories.recipes import listing
from core.factories.recipes.base import Recipe
from core.factories.recipes.items.base import ItemRecipe


# noinspection PyTypeChecker
@listing.register
class RangedWeaponRecipe(Recipe):
    name = "Base Ranged Weapon Recipe"
    base_object_type = RangedWeapon
    depends_on = [ItemRecipe]

    @staticmethod
    def build_components(item_type, game):
        new_components = [
            components.Melee(
                melee_damage=item_type.melee_damage,
                weapon_type=get_melee_weapon_types(item_type),
            ),
            components.Ranged(
                range_set=item_type.ranged_range,
                ammunition_type=item_type.ranged_ammunition_type,
            ),
        ]

        return new_components
