from bflib import units
from bflib.items import coins, listing
from bflib.items.writing.common import Scroll
from bflib.sizes import Size


@listing.register_type
@listing.register_item
class MagicScroll(Scroll):
    name = "Magic Scroll"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)
