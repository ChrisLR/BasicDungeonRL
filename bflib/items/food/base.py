from bflib.items import listing
from bflib.items.base import Item


@listing.register_type
class Food(Item):
    pass
