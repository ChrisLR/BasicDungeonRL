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
class LightQuarrel(Bolt):
    name = "Light Quarrel"

    ammunition_type = Bolt
    ammunition_damage = dice.D6(1)
    price = coins.Silver(2)
    weight = units.Pound(0.1)


@listing.register_item
class HeavyQuarrel(Bolt):
    name = "Heavy Quarrel"

    ammunition_type = Bolt
    ammunition_damage = dice.D8(1)
    price = coins.Silver(4)
    weight = units.Pound(0.1)


@listing.register_item
class ShortbowArrow(Arrow):
    name = "Shortbow Arrow"

    ammunition_type = Arrow
    ammunition_damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)


@listing.register_item
class LongbowArrow(Arrow):
    name = "Longbow Arrow"

    ammunition_type = Arrow
    ammunition_damage = dice.D6(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)


@listing.register_item
class SlingBullet(Bullet):
    name = "Sling Bullet"

    ammunition_type = Bullet
    ammunition_damage = dice.D4(1)
    price = coins.Silver(1)
    weight = units.Pound(0.1)
