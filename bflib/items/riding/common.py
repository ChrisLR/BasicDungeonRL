from bflib import units
from bflib.items import coins
from bflib.items.riding.base import RidingItem


class BitAndBridle(RidingItem):
    name = "Bit And Bridle"

    price = coins.Silver(15)
    weight = units.Pound(3)


class Horseshoes(RidingItem):
    name = "Horseshoes"

    price = coins.Gold(1)
    weight = units.Pound(10)


class SaddlePack(RidingItem):
    name = "Saddle, Pack"

    price = coins.Gold(5)
    weight = units.Pound(15)


class SaddleRiding(RidingItem):
    name = "Saddle, Riding"

    price = coins.Gold(10)
    weight = units.Pound(35)
