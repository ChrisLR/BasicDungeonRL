from bflib.items import weapons
from bflib.items import ammunition


class MagicWeaponRow(object):
    __slots__ = ["min_percent", "max_percent", "weapon_type"]

    def __init__(self, min_percent, max_percent, weapon_type):
        self.min_percent = min_percent
        self.max_percent = max_percent
        self.weapon_type = weapon_type


class MagicWeaponTable(object):
    rows = [
        MagicWeaponRow(1, 2, weapons.GreatAxe),
        MagicWeaponRow(3, 9, weapons.BattleAxe),
        MagicWeaponRow(10, 11, weapons.HandAxe),
        MagicWeaponRow(12, 19, weapons.Shortbow),
        MagicWeaponRow(20, 27, ammunition.ShortbowArrow),
        MagicWeaponRow(28, 31, weapons.Longbow),
        MagicWeaponRow(32, 35, ammunition.LongbowArrow),
        MagicWeaponRow(36, 43, ammunition.LightQuarrel),
        MagicWeaponRow(44, 47, ammunition.HeavyQuarrel),
        MagicWeaponRow(48, 59, weapons.Dagger),
        MagicWeaponRow(60, 65, weapons.Shortsword),
        MagicWeaponRow(66, 79, weapons.Longsword),
        MagicWeaponRow(80, 81, weapons.Scimitar),
        MagicWeaponRow(82, 83, weapons.TwoHandedSword),
        MagicWeaponRow(84, 86, weapons.Warhammer),
        MagicWeaponRow(87, 94, weapons.Mace),
        MagicWeaponRow(95, 95, weapons.Maul),
        MagicWeaponRow(96, 96, weapons.Polearm),
        MagicWeaponRow(97, 97, ammunition.SlingBullet),
        MagicWeaponRow(98, 100, weapons.Spear),
    ]

    @classmethod
    def get(cls, roll_value):
        return next((row for row in cls.rows
                     if row.min_percent <= roll_value <= row.max_percent))
