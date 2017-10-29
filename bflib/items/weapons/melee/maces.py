from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
class Bludgeon(MeleeWeapon):
    pass


@listing.register_item
class Club(Bludgeon):
    name = "Club"

    melee_damage = dice.D4(1)
    price = coins.Silver(2)
    size = Size.Medium
    weight = units.Pound(1)


@listing.register_item
class Cudgel(Bludgeon):
    name = "Cudgel"

    melee_damage = dice.D4(1)
    price = coins.Silver(2)
    size = Size.Medium
    weight = units.Pound(1)


@listing.register_item
class LightMace(Bludgeon):
    name = "Light Mace"

    melee_damage = dice.D6(1)
    price = coins.Gold(5)
    size = Size.Small
    weight = units.Pound(5)


@listing.register_item
class Mace(Bludgeon):
    name = "Mace"

    melee_damage = dice.D8(1)
    price = coins.Gold(6)
    size = Size.Medium
    weight = units.Pound(10)


@listing.register_item
class Maul(Bludgeon):
    name = "Maul"

    melee_damage = dice.D10(1)
    price = coins.Gold(10)
    size = Size.Large
    weight = units.Pound(16)


@listing.register_item
class Warhammer(Bludgeon):
    name = "Maul"

    melee_damage = dice.D6(1)
    price = coins.Gold(4)
    size = Size.Small
    weight = units.Pound(6)
