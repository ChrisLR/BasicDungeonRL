from bflib import dice
from bflib import units
from bflib.items import coins
from bflib.items.ammunition.base import Ammunition


class Arrow(Ammunition):
    pass


class Bolt(Ammunition):
    pass


class Bullet(Ammunition):
    pass


class ShortbowArrow(Arrow):
    name = "Shortbow Arrow"

    ammunition_type = Arrow
    ammunition_damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)


class SlingBullet(Bullet):
    name = "Shortbow Arrow"

    ammunition_type = Bullet
    ammunition_damage = dice.D4(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)
