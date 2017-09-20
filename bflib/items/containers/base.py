from bflib import units
from bflib.items.base import Item


class Container(Item):
    volume_limit = units.CubicFeet
    weight_limit = units.Pound


class LiquidContainer(Item):
    volume_limit = units.Litre


class SpecialContainer(Item):
    containable_items = tuple()
    max_quantity = 0
