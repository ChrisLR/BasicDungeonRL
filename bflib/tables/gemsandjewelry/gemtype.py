from bflib.items import gems


class GemTypeRow(object):
    __slots__ = ["min_percent", "max_percent", "gem_type"]

    def __init__(self, min_percent, max_percent, gem_type):
        self.min_percent = min_percent
        self.max_percent = max_percent
        self.gem_type = gem_type


class GemTypeTable(object):
    rows = [
        GemTypeRow(1, 10, gems.Greenstone),
        GemTypeRow(11, 20, gems.Malachite),
        GemTypeRow(21, 28, gems.Aventurine),
        GemTypeRow(29, 38, gems.Phenalope),
        GemTypeRow(39, 45, gems.Amethyst),
        GemTypeRow(46, 54, gems.Fluorospar),
        GemTypeRow(55, 60, gems.Garnet),
        GemTypeRow(61, 65, gems.Alexandrite),
        GemTypeRow(66, 70, gems.Topaz),
        GemTypeRow(71, 75, gems.Bloodstone),
        GemTypeRow(76, 79, gems.Sapphire),
        GemTypeRow(80, 89, gems.Diamond),
        GemTypeRow(90, 94, gems.FireOpal),
        GemTypeRow(95, 97, gems.Ruby),
        GemTypeRow(98, 100, gems.Emerald),
    ]

    @classmethod
    def get(cls, roll_value):
        return next((row for row in cls.rows
                     if row.min_percent <= roll_value <= row.max_percent))
