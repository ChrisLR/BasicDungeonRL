from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
@listing.register_item
class Dagger(MeleeWeapon):
    name = "Dagger"

    melee_damage = dice.D4(1)
    price = coins.Gold(2)
    size = Size.Small
    weight = units.Pound(1)
