from bflib.keywords.specialability import TurnUndeadKeyword


class TurnUndeadTable(object):
    inner_table = {cell.cleric_level: cell for cell in (
        TurnUndeadRow(
            1,
            TurnUndeadCell(1, 13),
            TurnUndeadCell(2, 17),
            TurnUndeadCell(3, 19),
            TurnUndeadCell(4, TurnUndeadKeyword.No),
            TurnUndeadCell(5, TurnUndeadKeyword.No),
            TurnUndeadCell(6, TurnUndeadKeyword.No),
            TurnUndeadCell(7, TurnUndeadKeyword.No),
            TurnUndeadCell(8, TurnUndeadKeyword.No),
            TurnUndeadCell(9, TurnUndeadKeyword.No),
        ),
        TurnUndeadRow(
            2,
            TurnUndeadCell(1, 11),
            TurnUndeadCell(2, 15),
            TurnUndeadCell(3, 18),
            TurnUndeadCell(4, 20),
            TurnUndeadCell(5, TurnUndeadKeyword.No),
            TurnUndeadCell(6, TurnUndeadKeyword.No),
            TurnUndeadCell(7, TurnUndeadKeyword.No),
            TurnUndeadCell(8, TurnUndeadKeyword.No),
            TurnUndeadCell(9, TurnUndeadKeyword.No),
        ),
        TurnUndeadRow(
            3,
            TurnUndeadCell(1, 9),
            TurnUndeadCell(2, 13),
            TurnUndeadCell(3, 17),
            TurnUndeadCell(4, 19),
            TurnUndeadCell(5, TurnUndeadKeyword.No),
            TurnUndeadCell(6, TurnUndeadKeyword.No),
            TurnUndeadCell(7, TurnUndeadKeyword.No),
            TurnUndeadCell(8, TurnUndeadKeyword.No),
            TurnUndeadCell(9, TurnUndeadKeyword.No),
        ),
        TurnUndeadRow(
            4,
            TurnUndeadCell(1, 7),
            TurnUndeadCell(2, 11),
            TurnUndeadCell(3, 15),
            TurnUndeadCell(4, 18),
            TurnUndeadCell(5, 20),
            TurnUndeadCell(6, TurnUndeadKeyword.No),
            TurnUndeadCell(7, TurnUndeadKeyword.No),
            TurnUndeadCell(8, TurnUndeadKeyword.No),
            TurnUndeadCell(9, TurnUndeadKeyword.No),
        ),
        TurnUndeadRow(
            5,
            TurnUndeadCell(1, 5),
            TurnUndeadCell(2, 9),
            TurnUndeadCell(3, 13),
            TurnUndeadCell(4, 18),
            TurnUndeadCell(5, 20),
            TurnUndeadCell(6, TurnUndeadKeyword.No),
            TurnUndeadCell(7, TurnUndeadKeyword.No),
            TurnUndeadCell(8, TurnUndeadKeyword.No),
            TurnUndeadCell(9, TurnUndeadKeyword.No),
        ),
    )}


class TurnUndeadCell(object):
    __slots__ = ["undead_hit_dice", "turn_keyword"]

    def __init__(self, undead_hit_dice, turn_keyword):
        self.undead_hit_dice = undead_hit_dice
        self.turn_keyword = turn_keyword


class TurnUndeadRow(object):
    __slots__ = ["cleric_level", "cells"]

    def __init__(self, cleric_level, *cells):
        self.cleric_level = cleric_level
        self.cells = cells