from bflib import units
from bflib.items import listing
from bflib.items.base import Item
from bflib.keywords.items import WearLocation


@listing.register_type
class Armor(Item):
    armor_class = 0
    armor_type = None
    wear_locations = WearLocation,
    weight = units.Pound


@listing.register_type
class Clothing(Armor):
    pass


@listing.register_type
class LightArmor(Armor):
    pass


@listing.register_type
class HeavyArmor(Armor):
    pass
