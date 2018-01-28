from bflib import dice
from bflib.tables.gemsandjewelry.qualitytype import QualityType


class GJQRow(object):
    __slots__ = ["min_percent", "max_percent", "quality_type", "value_in_gp", "number_found"]

    def __init__(self, min_percent, max_percent, quality_type, value_in_gp, number_found):
        self.min_percent = min_percent
        self.max_percent = max_percent
        self.quality_type = quality_type
        self.value_in_gp = value_in_gp
        self.number_found = number_found


class GemsAndJewelryQualityTable(object):
    rows = [
        GJQRow(0, 20, QualityType.Ornamental, 10, dice.D10(1)),
        GJQRow(21, 45, QualityType.Semiprecious, 50, dice.D8(1)),
        GJQRow(46, 75, QualityType.Fancy, 100, dice.D6(1)),
        GJQRow(76, 95, QualityType.Precious, 500, dice.D4(1)),
        GJQRow(96, 100, QualityType.Gem, 1000, dice.D2(1)),
        GJQRow(None, None, QualityType.Fancy, 5000, 1),
    ]
    _inner_table = {row.quality_type: row for row in rows}

    @classmethod
    def get_row_from_percent(cls, percent):
        return next((row for row in cls.rows if row.min_percent <= percent <= row.max_percent))

    @classmethod
    def get_row_from_quality(cls, quality_type):
        return cls._inner_table.get(quality_type)
