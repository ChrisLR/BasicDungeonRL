class ExperienceTable(object):
    inner_table = {
        row.hit_dice: row for row in
        (
            ExperienceRow(0, 10, 3),
            ExperienceRow(1, 25, 12),
            ExperienceRow(2, 75, 25),
            ExperienceRow(3, 145, 30),
            ExperienceRow(4, 240, 40),
            ExperienceRow(5, 360, 45),
            ExperienceRow(6, 500, 55),
            ExperienceRow(7, 670, 65),
            ExperienceRow(8, 875, 70),
            ExperienceRow(9, 1075, 75),
            ExperienceRow(10, 1300, 90),
            ExperienceRow(11, 1575, 95),
            ExperienceRow(12, 1875, 100),
            ExperienceRow(13, 2175, 110),
            ExperienceRow(14, 2500, 115),
            ExperienceRow(15, 2850, 125),
            ExperienceRow(16, 3250, 135),
            ExperienceRow(17, 3600, 145),
            ExperienceRow(18, 4000, 160),
            ExperienceRow(19, 4500, 175),
            ExperienceRow(20, 5250, 200),
            ExperienceRow(21, 6000, 225),
            ExperienceRow(22, 6750, 250),
            ExperienceRow(23, 7500, 275),
            ExperienceRow(24, 8250, 300),
            ExperienceRow(25, 9000, 325)
        )
    }

    @classmethod
    def get(cls, hit_die_value, include_bonus=0):
        if hit_die_value < 1:
            row = cls.inner_table[0]
        elif hit_die_value > 25:
            last_row = cls.inner_table[-1]
            additional_dice = hit_die_value - 25

            row = ExperienceRow(
                hit_die_value,
                last_row.xp_value + (750 * additional_dice),
                last_row.special_ability_bonus + (25 * additional_dice)
            )
        else:
            row = cls.inner_table[hit_die_value]

        return row.xp_value + (row.special_ability_bonus * include_bonus)


class ExperienceRow(object):
    __slots__ = ["hit_dice", "xp_value", "special_ability_bonus"]

    def __init__(self, hit_dice, xp_value, special_ability_bonus):
        self.hit_dice = hit_dice
        self.xp_value = xp_value
        self.special_ability_bonus = special_ability_bonus
