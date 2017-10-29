from bflib import units
from bflib.items import coins, listing
from bflib.items.containers.base import SpecialContainer
from bflib.keywords.items import WearLocation
from bflib.sizes import Size
from bflib.items import writing
from bflib.items.ammunition.common import Arrow, Bolt


@listing.register_item
class BoltCase(SpecialContainer):
    name = "Bolt Case"

    container_type = SpecialContainer
    containable_items = Bolt,
    max_quantity = 20
    price = coins.Gold(1)
    size = Size.Medium
    weight = units.Pound(1)
    wear_locations = WearLocation.Back,


@listing.register_item
class ScrollCase(SpecialContainer):
    name = "Scroll Case"

    container_type = SpecialContainer
    containable_items = writing.Scroll, writing.Map
    max_quantity = 10
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.5)
    wear_locations = WearLocation.Belt, WearLocation.Bandolier


@listing.register_item
class Quiver(SpecialContainer):
    name = "Quiver"

    container_type = SpecialContainer
    containable_items = Arrow,
    max_quantity = 20
    price = coins.Gold(1)
    size = Size.Medium
    weight = units.Pound(1)
    wear_locations = WearLocation.Back,
