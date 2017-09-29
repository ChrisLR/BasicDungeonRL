from bflib import dice
from bflib import units
from bflib.items import coins
from bflib.items.weapons.base import Weapon
from bflib.sizes import Size


class MeleeWeapon(Weapon):
    damage = None


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


class Polearm(MeleeWeapon):
    pass


class Quarterstaff(MeleeWeapon):
    pass


class WalkingStaff(Club):
    name = "Walking Staff"


class Warhammer(MeleeWeapon):
    pass
