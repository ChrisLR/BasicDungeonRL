from bflib import dice, units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
class Sword(MeleeWeapon):
    pass


@listing.register_item
class Shortsword(Sword):
    name = "Shortsword"

    melee_damage = dice.D6(1)
    price = coins.Gold(6)
    size = Size.Small
    weight = units.Pound(3)


@listing.register_item
class Longsword(Sword):
    name = "Longsword"

    melee_damage = dice.D8(1)
    price = coins.Gold(10)
    size = Size.Medium
    weight = units.Pound(4)


@listing.register_item
class Scimitar(Sword):
    name = "Scimitar"

    melee_damage = dice.D8(1)
    price = coins.Gold(10)
    size = Size.Medium
    weight = units.Pound(4)


@listing.register_item
class TwoHandedSword(MeleeWeapon):
    name = "Two-Handed Sword"

    melee_damage = dice.D10(1)
    price = coins.Gold(18)
    size = Size.Large
    weight = units.Pound(10)
