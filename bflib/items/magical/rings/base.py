from bflib import units
from bflib.items import coins, listing
from bflib.items.jewelry.base import Jewelry
from bflib.items.magical.base import MagicItem
from bflib.sizes import Size


@listing.register_type
class Ring(Jewelry, MagicItem):
    name = "Ring"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)
