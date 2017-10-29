from bflib import units
from bflib.items import listing
from bflib.items.base import Item


@listing.register_type
class ClimbingTool(Item):
    height = units.Feet


@listing.register_type
class Tool(Item):
    pass
