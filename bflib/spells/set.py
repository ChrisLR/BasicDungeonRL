class SpellSlotSet(object):
    __slots__ = ["level_1", "level_2", "level_3", "level_4", "level_5", "level_6"]

    def __init__(self, level_1=0, level_2=0, level_3=0, level_4=0, level_5=0, level_6=0):
        self.level_1 = level_1
        self.level_2 = level_2
        self.level_3 = level_3
        self.level_4 = level_4
        self.level_5 = level_5
        self.level_6 = level_6


class SpellSet(object):
    __slots__ = ["spells"]

    def __init__(self, spells):
        self.spells = {spell.level: spell for spell in spells}
