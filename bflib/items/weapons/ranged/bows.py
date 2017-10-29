from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.ranged.base import RangedWeapon
from bflib.sizes import Size
from bflib.rangeset import RangeSet


@listing.register_type
class Bow(RangedWeapon):
    pass


@listing.register_item
class Shortbow(Bow):
    name = "Shortbow"

    melee_damage = dice.D2(1)
    ranged_range = RangeSet(units.Feet(50), units.Feet(100), units.Feet(150))
    ranged_damage = None
    ranged_ammunition_type = None

    price = coins.Gold(2)
    size = Size.Small
    weight = units.Pound(1)


class Longbow(Bow):
    name = "Longbow"
