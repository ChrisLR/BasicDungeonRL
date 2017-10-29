from bflib.items import listing
from bflib.items.weapons.base import Weapon


@listing.register_type
class MeleeWeapon(Weapon):
    melee_damage = None
