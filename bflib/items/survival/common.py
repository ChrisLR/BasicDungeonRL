from bflib import units
from bflib.items import coins, listing
from bflib.items.survival.base import SurvivalItem
from bflib.sizes import Size


@listing.register_item
class LargeTent(SurvivalItem):
    name = "Tent, Large"

    size = Size.Large
    price = coins.Gold(25)
    weight = units.Pound(20)


@listing.register_item
class SmallTent(SurvivalItem):
    name = "Tent, Small"

    size = Size.Medium
    price = coins.Gold(5)
    weight = units.Pound(10)


@listing.register_item
class WinterBlanket(SurvivalItem):
    name = "Winter Blanket"

    size = Size.Medium
    price = coins.Gold(1)
    weight = units.Pound(3)
