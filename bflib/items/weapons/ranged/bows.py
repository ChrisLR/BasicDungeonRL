from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.ammunition.common import ShortbowArrow, LongbowArrow
from bflib.items.weapons.ranged.base import RangedWeapon
from bflib.rangeset import RangeSet
from bflib.sizes import Size


@listing.register_type
class Bow(RangedWeapon):
    pass


@listing.register_item
class Shortbow(Bow):
    name = "Shortbow"

    melee_damage = dice.D2(1)
    ranged_range = RangeSet(units.Feet(50), units.Feet(100), units.Feet(150))
    ranged_damage = None
    ranged_ammunition_type = ShortbowArrow

    price = coins.Gold(2)
    size = Size.Small
    weight = units.Pound(1)


@listing.register_item
class Longbow(Bow):
    name = "Longbow"

    melee_damage = dice.D2(1)
    ranged_range = RangeSet(units.Feet(70), units.Feet(140), units.Feet(210))
    ranged_damage = None
    ranged_ammunition_type = LongbowArrow

    price = coins.Silver(2)
    size = Size.Large
    weight = units.Pound(3)
