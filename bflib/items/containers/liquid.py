from bflib import units
from bflib.items import coins, listing
from bflib.items.containers.base import LiquidContainer
from bflib.sizes import Size


@listing.register_item
class GlassBottle(LiquidContainer):
    name = "Glass Bottle"

    container_type = LiquidContainer
    volume_limit = units.Litre(0.250)
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.1)


@listing.register_item
class Waterskin(LiquidContainer):
    name = "Waterskin"

    container_type = LiquidContainer
    volume_limit = units.Litre(1)
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(2)


@listing.register_item
class Vial(LiquidContainer):
    name = "Vial"

    container_type = LiquidContainer
    volume_limit = units.Litre(0.250)
    price = coins.Gold(1)
    size = Size.Small
    weight = units.Pound(0.1)
