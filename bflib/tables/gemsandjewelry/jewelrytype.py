from bflib.items import jewelry


class JewelryTypeRow(object):
    __slots__ = ["min_percent", "max_percent", "jewelry_type"]

    def __init__(self, min_percent, max_percent, jewelry_type):
        self.min_percent = min_percent
        self.max_percent = max_percent
        self.jewelry_type = jewelry_type


class JewelryTypeTable(object):
    rows = [
        JewelryTypeRow(1, 6, jewelry.Anklet),
        JewelryTypeRow(7, 12, jewelry.Belt),
        JewelryTypeRow(13, 14, jewelry.Bowl),
        JewelryTypeRow(15, 21, jewelry.Bracelet),
        JewelryTypeRow(16, 27, jewelry.Brooch),
        JewelryTypeRow(28, 32, jewelry.Buckle),
        JewelryTypeRow(33, 37, jewelry.Chain),
        JewelryTypeRow(38, 40, jewelry.Choker),
        JewelryTypeRow(41, 42, jewelry.Circlet),
        JewelryTypeRow(46, 47, jewelry.Clasp),
        JewelryTypeRow(48, 51, jewelry.Comb),
        JewelryTypeRow(52, 52, jewelry.Crown),
        JewelryTypeRow(53, 55, jewelry.Cup),
        JewelryTypeRow(56, 62, jewelry.Earring),
        JewelryTypeRow(63, 65, jewelry.Flagon),
        JewelryTypeRow(66, 68, jewelry.Goblet),
        JewelryTypeRow(69, 73, jewelry.Knife),
        JewelryTypeRow(74, 77, jewelry.LetterOpener),
        JewelryTypeRow(78, 80, jewelry.Locket),
        JewelryTypeRow(81, 82, jewelry.Medal),
        JewelryTypeRow(83, 89, jewelry.Necklace),
        JewelryTypeRow(90, 95, jewelry.Pin),
        JewelryTypeRow(96, 96, jewelry.Sceptre),
        JewelryTypeRow(97, 99, jewelry.Statuette),
        JewelryTypeRow(100, 100, jewelry.Tiara),
    ]

    @classmethod
    def get(cls, roll_value):
        return next((row for row in cls.rows
                     if row.min_percent <= roll_value <= row.max_percent))
