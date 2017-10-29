from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.items.weapons.melee.axes import Axe
from bflib.items.weapons.melee.daggers import Dagger
from bflib.items.weapons.melee.maces import Bludgeon
from bflib.items.weapons.melee.polearms import Polearm
from bflib.items.weapons.melee.spears import Spear
from bflib.items.weapons.melee.staves import Staff
from bflib.items.weapons.melee.swords import Sword

melee_weapon_types = [
    Axe,
    Bludgeon,
    Dagger,
    Polearm,
    Spear,
    Staff,
    Sword,
]


def get_melee_weapon_types(base_item_type):
    for weapon_type in melee_weapon_types:
        if issubclass(base_item_type, weapon_type):
            return weapon_type

    return MeleeWeapon
