from bflib import units
from bflib.items import coins
from bflib.items.containers.base import LiquidContainer
from bflib.sizes import Size


class GlassBottle(LiquidContainer):
    name = "Glass Bottle"
    volume_limit = units.Litre(0.250)
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.1)


class Waterskin(LiquidContainer):
    name = "Waterskin"
    volume_limit = units.Litre(1)
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(2)


class Vial(LiquidContainer):
    name = "Vial"
    volume_limit = units.Litre(0.250)
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.1)
