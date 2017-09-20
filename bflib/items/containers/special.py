from bflib import units
from bflib.items import coins
from bflib.items.containers.base import SpecialContainer
from bflib.keywords.items import WearLocation
from bflib.sizes import Size
from bflib.items import writing
from bflib.items.ammunition.common import Arrow, Bolt


class BoltCase(SpecialContainer):
    name = "Bolt Case"

    containable_items = Bolt,
    max_quantity = 20
    price = coins.Gold(1)
    size = Size.Medium
    weight = units.Pound(1)
    wear_locations = WearLocation.Back


class ScrollCase(SpecialContainer):
    name = "Scroll Case"

    containable_items = writing.Scroll, writing.Map
    max_quantity = 10
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.5)
    wear_locations = WearLocation.Belt, WearLocation.Bandolier


class Quiver(SpecialContainer):
    name = "Quiver"

    containable_items = Arrow,
    max_quantity = 20
    price = coins.Gold(1)
    size = Size.Medium
    weight = units.Pound(1)
    wear_locations = WearLocation.Back
