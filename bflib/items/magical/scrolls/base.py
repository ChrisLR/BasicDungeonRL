from bflib import units
from bflib.items import coins, listing
from bflib.items.magical.base import MagicItem
from bflib.items.writing.common import Scroll
from bflib.sizes import Size


@listing.register_type
class MagicScroll(Scroll, MagicItem):
    name = "Magic Scroll"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)
