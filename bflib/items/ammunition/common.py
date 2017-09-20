from bflib import dice
from bflib import units
from bflib.items import coins
from bflib.items.ammunition.base import Ammunition


class Arrow(Ammunition):
    pass


class Bolt(Ammunition):
    pass


class ShortbowArrow(Arrow):
    name = "Shortbow Arrow"

    damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)
