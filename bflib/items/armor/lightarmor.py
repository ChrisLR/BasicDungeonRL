from bflib import units
from bflib.items import coins
from bflib.items.armor.base import LightArmor
from bflib.keywords.items import WearLocation
from bflib.sizes import Size


class PaddedArmor(LightArmor):
    name = "Padded Armor"

    armor_class = 12
    armor_type = LightArmor
    price = coins.Gold(15)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(10)


class HideArmor(LightArmor):
    name = "Hide Armor"

    armor_class = 13
    armor_type = LightArmor
    price = coins.Gold(10)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(30)


class LeatherArmor(LightArmor):
    name = "Leather Armor"

    armor_class = 13
    armor_type = LightArmor
    price = coins.Gold(20)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(15)


class StuddedLeatherArmor(LightArmor):
    name = "Studded Leather Armor"

    armor_class = 14
    armor_type = LightArmor
    price = coins.Gold(25)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(30)
