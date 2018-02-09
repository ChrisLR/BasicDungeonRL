from bflib.items import listing
from bflib.items.base import Item


@listing.register_type
class Potion(Item):
    effect = None
