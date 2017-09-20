from bflib import units
from bflib.sizes import Size


class Item(object):
    name = ""

    price = None
    size = Size.Medium
    wear_locations = tuple()
    weight = units.Pound
