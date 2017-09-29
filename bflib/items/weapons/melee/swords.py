from bflib import dice
from bflib import units
from bflib.items import coins
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


class Sword(MeleeWeapon):
    pass


class Shortsword(Sword):
    name = "Shortsword"

    damage = dice.D6(1)
    price = coins.Gold(6)
    size = Size.Small
    weight = units.Pound(3)


class Longsword(Sword):
    name = "Longsword"

    damage = dice.D8(1)
    price = coins.Gold(10)
    size = Size.Medium
    weight = units.Pound(4)


class Scimitar(Sword):
    name = "Scimitar"

    damage = dice.D8(1)
    price = coins.Gold(10)
    size = Size.Medium
    weight = units.Pound(4)


class TwoHandedSword(MeleeWeapon):
    name = "Two-Handed Sword"

    damage = dice.D10(1)
    price = coins.Gold(18)
    size = Size.Large
    weight = units.Pound(10)
