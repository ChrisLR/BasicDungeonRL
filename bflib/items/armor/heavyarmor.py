from bflib import units
from bflib.items import coins
from bflib.items.armor.base import HeavyArmor
from bflib.keywords.items import WearLocation
from bflib.sizes import Size


class RingMail(HeavyArmor):
    name = "Ring Mail"

    armor_class = 14
    armor_type = HeavyArmor
    price = coins.Gold(25)
    size = Size.Medium
    wear_locations = WearLocation.Torso, WearLocation.Legs
    weight = units.Pound(30)


class ChainMail(HeavyArmor):
    name = "Chain Mail"

    armor_class = 15
    armor_type = HeavyArmor
    price = coins.Gold(60)
    size = Size.Medium
    wear_locations = WearLocation.Torso, WearLocation.Legs
    weight = units.Pound(40)


class ScaleMail(HeavyArmor):
    name = "Scale Mail"

    armor_class = 16
    armor_type = HeavyArmor
    price = coins.Gold(80)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(55)


class SplintMail(HeavyArmor):
    name = "Splint Mail"

    armor_class = 16
    armor_type = HeavyArmor
    price = coins.Gold(100)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(45)


class PlateMail(HeavyArmor):
    name = "Plate Mail"

    armor_class = 17
    armor_type = HeavyArmor
    price = coins.Gold(300)
    size = Size.Medium
    wear_locations = WearLocation.Torso,
    weight = units.Pound(50)


class FieldPlateMail(HeavyArmor):
    name = "Field Plate Mail"

    armor_class = 18
    armor_type = HeavyArmor
    price = coins.Gold(500)
    size = Size.Medium
    wear_locations = (
        WearLocation.Torso,
        WearLocation.Arms,
        WearLocation.Hands,
        WearLocation.Legs,
        WearLocation.Feet,
    )
    weight = units.Pound(70)


class FullPlateMail(HeavyArmor):
    name = "Full Plate Mail"

    armor_class = 19
    armor_type = HeavyArmor
    price = coins.Gold(1500)
    size = Size.Medium
    wear_locations = (
        WearLocation.Torso,
        WearLocation.Arms,
        WearLocation.Hands,
        WearLocation.Legs,
        WearLocation.Feet,
    )
    weight = units.Pound(80)
