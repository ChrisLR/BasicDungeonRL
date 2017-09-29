from bflib import dice
from bflib import units
from bflib.items import coins
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


class Dagger(MeleeWeapon):
    name = "Dagger"

    damage = dice.D4(1)
    price = coins.Gold(2)
    size = Size.Small
    weight = units.Pound(1)
