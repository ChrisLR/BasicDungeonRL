from bflib import units
from bflib.items import coins
from bflib.items.shields.base import Shield
from bflib.keywords.items import WieldLocation
from bflib.sizes import Size


class Buckler(Shield):
    name = "Buckler"

    armor_class_melee = 1
    armor_class_missile = 0
    price = coins.Gold(5)
    size = Size.Small
    wield_locations = WieldLocation.Any,
    weight = units.Pound(2)


class MediumShield(Shield):
    name = "Medium Shield"

    armor_class_melee = 1
    armor_class_missile = 1
    price = coins.Gold(7)
    size = Size.Medium
    wield_locations = WieldLocation.Any,
    weight = units.Pound(7)


class TowerShield(Shield):
    name = "Tower Shield"

    armor_class_melee = 1
    armor_class_missile = 3
    price = coins.Gold(15)
    size = Size.Medium
    wield_locations = WieldLocation.Any,
    weight = units.Pound(12)
