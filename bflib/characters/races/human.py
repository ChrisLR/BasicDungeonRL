from datetime import timedelta

from bflib import languages
from bflib import restrictions
from bflib import units
from bflib.characters import specialabilities, savingthrows
from bflib.characters.races.base import Race


class Human(Race):
    name = "Human"
    average_height = units.Feet(6)
    average_weight = units.Pound(175)
    average_lifespan = timedelta(days=27375)

    restriction_set = restrictions.RestrictionSet(
        classes=restrictions.ClassRestrictionSet()
    )
    racial_language = languages.Common
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.ExperienceBonus(10)
    ))
    saving_throw_set = savingthrows.SavingThrowSet()
