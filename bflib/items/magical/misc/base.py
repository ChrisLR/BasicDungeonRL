from bflib import units
from bflib.items import coins, listing
from bflib.items.jewelry.base import Jewelry
from bflib.items.magical.base import MagicItem
from bflib.sizes import Size


@listing.register_type
class MiscMagical(Jewelry, MagicItem):
    name = "Misc Magical"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)
