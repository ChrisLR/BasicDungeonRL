from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
@listing.register_item
class Polearm(MeleeWeapon):
    name = "Polearm"

    melee_damage = dice.D10(1)
    price = coins.Gold(9)
    size = Size.Large
    weight = units.Pound(15)
