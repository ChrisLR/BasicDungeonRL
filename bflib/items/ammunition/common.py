from bflib import dice
from bflib import units
from bflib.items import coins, listing
from bflib.items.ammunition.base import Ammunition


@listing.register_type
class Arrow(Ammunition):
    pass


@listing.register_type
class Bolt(Ammunition):
    pass


@listing.register_type
class Bullet(Ammunition):
    pass


@listing.register_item
class ShortbowArrow(Arrow):
    name = "Shortbow Arrow"

    ammunition_type = Arrow
    ammunition_damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)


@listing.register_item
class SlingBullet(Bullet):
    name = "Shortbow Arrow"

    ammunition_type = Bullet
    ammunition_damage = dice.D4(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)
