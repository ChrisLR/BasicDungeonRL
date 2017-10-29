from bflib import units
from bflib.items import coins, listing
from bflib.items.ammunition.common import Bullet
from bflib.items.weapons.ranged.base import RangedWeapon
from bflib.rangeset import RangeSet
from bflib.sizes import Size


@listing.register_type
@listing.register_item
class Sling(RangedWeapon):
    name = "Sling"

    ranged_range = RangeSet(units.Feet(30), units.Feet(60), units.Feet(90))
    ranged_damage = None
    ranged_ammunition_type = Bullet

    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.1)
