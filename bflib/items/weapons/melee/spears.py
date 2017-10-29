from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
@listing.register_item
class Spear(MeleeWeapon):
    name = "Spear"

    melee_damage = dice.D6(1)
    price = coins.Gold(5)
    size = Size.Medium
    weight = units.Pound(5)
