from bflib import units
from bflib.items import coins, listing
from bflib.items.armor.base import Clothing
from bflib.keywords.items import WearLocation


@listing.register_item
class Cloak(Clothing):
    name = "Cloak"

    armor_type = Clothing
    price = coins.Gold(2)
    wear_locations = WearLocation.Back,
    weight = units.Pound(1)


@listing.register_item
class CommonOutfit(Clothing):
    name = "Common Outfit"

    armor_type = Clothing
    wear_locations = (WearLocation.Torso, WearLocation.Legs, WearLocation.Feet, WearLocation.Arms),
    price = coins.Gold(4)
    weight = units.Pound(1)
