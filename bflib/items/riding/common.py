from bflib import units
from bflib.items import coins, listing
from bflib.items.riding.base import RidingItem


@listing.register_item
class BitAndBridle(RidingItem):
    name = "Bit And Bridle"

    price = coins.Silver(15)
    weight = units.Pound(3)


@listing.register_item
class Horseshoes(RidingItem):
    name = "Horseshoes"

    price = coins.Gold(1)
    weight = units.Pound(10)


@listing.register_item
class SaddlePack(RidingItem):
    name = "Saddle, Pack"

    price = coins.Gold(5)
    weight = units.Pound(15)


@listing.register_item
class SaddleRiding(RidingItem):
    name = "Saddle, Riding"

    price = coins.Gold(10)
    weight = units.Pound(35)
