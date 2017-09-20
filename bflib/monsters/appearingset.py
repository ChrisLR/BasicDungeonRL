from bflib import dice


class AppearingSet(object):
    __slots__ = ["dice_dungeon", "dice_wild", "dice_lair"]

    def __init__(self, dice_dungeon=None, dice_wild=None, dice_lair=None):
        self.dice_dungeon = dice_dungeon  # type: dice.Dice
        self.dice_wild = dice_wild  # type: dice.Dice
        self.dice_lair = dice_lair  # type: dice.Dice
