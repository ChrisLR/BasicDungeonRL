from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
class Staff(MeleeWeapon):
    pass


@listing.register_item
class Quarterstaff(Staff):
    name = "Quarterstaff"

    melee_damage = dice.D6(1)
    price = coins.Gold(2)
    size = Size.Large
    weight = units.Pound(4)


@listing.register_item
class WalkingStaff(Staff):
    name = "Walking Staff"

    melee_damage = dice.D4(1)
    price = coins.Silver(2)
    size = Size.Medium
    weight = units.Pound(1)
