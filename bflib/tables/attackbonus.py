class AttackBonusTable(object):
    inner_table = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 8,
        10: 9,
        11: 9,
        12: 10,
        13: 10,
        14: 11,
        15: 11,
        16: 12,
        17: 12,
        18: 12,
        19: 12,
        20: 13,
        21: 13,
        22: 13,
        23: 13,
        24: 14,
        25: 14,
        26: 14,
        27: 14,
        28: 15,
        29: 15,
        30: 15,
        31: 15
    }

    @classmethod
    def get_by_hit_dice(cls, hit_dice_value):
        if hit_dice_value < 1:
            return 0
        if hit_dice_value > 31:
            return 16
        else:
            return cls.inner_table[hit_dice_value]
