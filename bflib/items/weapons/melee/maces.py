from bflib import dice, units
from bflib.items import coins
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


class Club(MeleeWeapon):
    name = "Club"

    damage = dice.D4(1)
    price = coins.Silver(2)
    size = Size.Medium
    weight = units.Pound(1)


class Cudgel(Club):
    name = "Cudgel"


class Mace(MeleeWeapon):
    pass


class Maul(MeleeWeapon):
    pass


class Warhammer(MeleeWeapon):
    pass
