from bflib.tables.gemsandjewelry.qualitytype import (
    QualityType,
    get_quality_value,
    get_type_from_value
)

from bflib.tables.gemsandjewelry.qualitytable import GemsAndJewelryQualityTable


class VARow(object):
    __slots__ = ["result", "value_adjustment"]

    def __init__(self, result, value_adjustment):
        self.result = result
        self.value_adjustment = value_adjustment


class ValueAdjustmentTable(object):
    @classmethod
    def get(cls, roll_result, quality_type, gold_value):
        adjuster = cls._mapping.get(roll_result)
        if adjuster is None:
            return quality_type, gold_value

        quality_type, gold_value = adjuster(quality_type, gold_value)

        return quality_type, gold_value

    @classmethod
    def lower_row(cls, quality_type, _):
        quality_type_value = get_quality_value(quality_type)
        new_quality = get_type_from_value(quality_type_value - 1)
        row = GemsAndJewelryQualityTable.get_row_from_quality(new_quality)

        return new_quality, row.value_in_gp

    @classmethod
    def higher_row(cls, quality_type, _):
        quality_type_value = get_quality_value(quality_type)
        new_quality = get_type_from_value(quality_type_value + 1)
        row = GemsAndJewelryQualityTable.get_row_from_quality(new_quality)

        return new_quality, row.value_in_gp

    _mapping = {
        2: lower_row,
        3: lambda quality_type, gold_value: (quality_type, gold_value / 2),
        4: lambda quality_type, gold_value: (quality_type, round((gold_value / 4) * 3)),
        10: lambda quality_type, gold_value: (quality_type, round(gold_value * 1.5)),
        11: lambda quality_type, gold_value: (quality_type, gold_value * 2),
        12: higher_row
    }
