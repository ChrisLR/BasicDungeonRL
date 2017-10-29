from bflib import units
from bflib.items import coins, listing
from bflib.items.shields.base import Shield
from bflib.keywords.items import WieldLocation
from bflib.sizes import Size


@listing.register_item
class Buckler(Shield):
    name = "Buckler"

    armor_class_melee = 1
    armor_class_missile = 0
    price = coins.Gold(5)
    size = Size.Small
    wield_locations = WieldLocation.Any,
    weight = units.Pound(2)


@listing.register_item
class MediumShield(Shield):
    name = "Medium Shield"

    armor_class_melee = 1
    armor_class_missile = 1
    price = coins.Gold(7)
    size = Size.Medium
    wield_locations = WieldLocation.Any,
    weight = units.Pound(7)


@listing.register_item
class TowerShield(Shield):
    name = "Tower Shield"

    armor_class_melee = 1
    armor_class_missile = 3
    price = coins.Gold(15)
    size = Size.Medium
    wield_locations = WieldLocation.Any,
    weight = units.Pound(12)
