from bflib.characters.savingthrows import DeathPoison, DragonBreath, ParalysisStone, Spells, Wands


class SavingThrowSet(object):
    __slots__ = ["death_poison", "dragon_breath", "paralysis_stone", "spells", "wands"]

    def __init__(self, death_poison=0, dragon_breath=0, paralysis_stone=0, spells=0, wands=0):
        self.death_poison = DeathPoison(death_poison)
        self.dragon_breath = DragonBreath(dragon_breath)
        self.paralysis_stone = ParalysisStone(paralysis_stone)
        self.spells = Spells(spells)
        self.wands = Wands(wands)
