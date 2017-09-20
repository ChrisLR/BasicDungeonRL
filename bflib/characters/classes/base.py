from bflib import restrictions
from bflib.characters.classes.level import LevelTable
from bflib.characters.specialabilities import SpecialAbilitySet


class CharacterClass(object):
    name = ""
    restriction_set = restrictions.RestrictionSet()
    special_abilities = SpecialAbilitySet()
    level_table = LevelTable()

