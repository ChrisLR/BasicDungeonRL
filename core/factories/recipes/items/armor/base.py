from bflib import units
from bflib.items.base import Item
from bflib.keywords.items import WearLocation


class Armor(Item):
    armor_class = 0
    armor_type = None
    wear_locations = WearLocation,
    weight = units.Pound


class Clothing(Armor):
    pass


class LightArmor(Armor):
    pass


class HeavyArmor(Armor):
    pass
