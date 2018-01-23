from bflib.items.base import Item
from bflib.items import listing


@listing.register_type
class Potion(Item):
    pass
