from bflib import units
from bflib.items import coins, listing
from bflib.items.base import Item
from bflib.keywords.items import WieldLocation
from bflib.sizes import Size


@listing.register_type
class Shield(Item):
    name = "Shield"

    armor_class_melee = 0
    armor_class_missile = 0
    price = coins.Gold
    size = Size.Medium
    wield_locations = WieldLocation.Any,
    weight = units.Pound
