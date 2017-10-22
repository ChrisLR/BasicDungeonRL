from bflib import units
from bflib.items.base import Item


class Container(Item):
    container_type = None
    volume_limit = units.CubicFeet
    weight_limit = units.Pound


class LiquidContainer(Item):
    container_type = None
    volume_limit = units.Litre


class SpecialContainer(Item):
    container_type = None
    containable_items = tuple()
    max_quantity = 0
