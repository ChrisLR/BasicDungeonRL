import abc
from datetime import timedelta

from bflib import languages
from bflib import restrictions
from bflib import units
from bflib.characters import specialabilities, savingthrows


class Race(object):
    __metaclass__ = abc.ABCMeta

    name = ""
    average_height = units.Feet(0)
    average_weight = units.Pound(0)
    average_lifespan = timedelta(0)

    restriction_set = restrictions.RestrictionSet()
    racial_language = languages.Common
    special_ability_set = specialabilities.SpecialAbilitySet()
    saving_throw_set = savingthrows.SavingThrowSet()
