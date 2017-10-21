from bflib import units
from bflib.items import coins
from bflib.items.writing.common import Scroll
from bflib.sizes import Size


class MagicScroll(Scroll):
    name = "Magic Scroll"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)


class RandomMagicScroll(Scroll):
    name = "Magic Scroll"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)
    spell_level = 1
