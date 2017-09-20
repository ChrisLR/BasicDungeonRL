from bflib import units
from bflib.items import coins
from bflib.items.armor.base import Clothing
from bflib.keywords.items import WearLocation


class Cloak(Clothing):
    name = "Cloak"

    price = coins.Gold(2)
    wear_locations = WearLocation.Back,
    weight = units.Pound(1)


class CommonOutfit(Clothing):
    name = "Common Outfit"

    wear_locations = (WearLocation.Torso, WearLocation.Legs, WearLocation.Feet, WearLocation.Arms),
    price = coins.Gold(4)
    weight = units.Pound(1)
