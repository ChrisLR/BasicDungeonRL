from bflib.items.armor.base import Armor
from bflib.items.magical.misc.base import MiscMagical
from bflib.items.magical.rings.base import Ring
from bflib.items.magical.rods.base import Rod
from bflib.items.magical.scrolls.base import MagicScroll
from bflib.items.magical.staffs.base import MagicStaff
from bflib.items.magical.wands.base import Wand
from bflib.items.potions.base import Potion
from bflib.items.weapons.base import Weapon


class MagicItemTypeRow(object):
    __slots__ = [
        "min_percent", "max_percent",
        "weapon_armor_min", "weapon_armor_max",
        "non_weapon_min", "non_weapon_max", "item_type"]

    def __init__(self, min_percent, max_percent, weapon_armor_min, weapon_armor_max,
                 non_weapon_min, non_weapon_max, item_type):
        self.min_percent = min_percent
        self.max_percent = max_percent
        self.weapon_armor_min = weapon_armor_min
        self.weapon_armor_max = weapon_armor_max
        self.non_weapon_min = non_weapon_min
        self.non_weapon_max = non_weapon_max
        self.item_type = item_type


class MagicItemTypeTable(object):
    rows = [
        MagicItemTypeRow(1, 25, 1, 70, None, None, Weapon),
        MagicItemTypeRow(26, 35, 71, 100, 1, 12, Armor),
        MagicItemTypeRow(36, 55, None, None, 13, 40, Potion),
        MagicItemTypeRow(56, 85, None, None, 41, 79, MagicScroll),
        MagicItemTypeRow(86, 90, None, None, 80, 86, Ring),
        MagicItemTypeRow(91, 95, None, None, 87, 93, (Wand, MagicStaff, Rod)),
        MagicItemTypeRow(96, 100, None, None, 94, 100, MiscMagical),
    ]

    @classmethod
    def get_any(cls, roll_value):
        return next((row for row in cls.rows
                     if row.min_percent <= roll_value <= row.max_percent))

    @classmethod
    def get_non_weapon(cls, roll_value):
        return next((row for row in cls.rows
                     if row.non_weapon_min <= roll_value <= row.non_weapon_max))

    @classmethod
    def get_weapon_armor(cls, roll_value):
        return next((row for row in cls.rows
                     if row.weapon_armor_min <= roll_value <= row.weapon_armor_max))
