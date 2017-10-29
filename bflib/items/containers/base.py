from bflib import units
from bflib.items import listing
from bflib.items.base import Item


@listing.register_type
class Container(Item):
    container_type = None
    volume_limit = units.CubicFeet
    weight_limit = units.Pound


@listing.register_type
class LiquidContainer(Item):
    container_type = None
    volume_limit = units.Litre


@listing.register_type
class SpecialContainer(Item):
    container_type = None
    containable_items = tuple()
    max_quantity = 0
