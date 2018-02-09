from datetime import timedelta

from bflib import languages, restrictions, units
from bflib.characters import abilityscores, classes, specialabilities, \
    racialclass
from bflib.characters.races.base import Race


class Bugbear(Race):
    name = "Bugbear"
    average_height = units.Feet(6)
    average_weight = units.Pound(180)
    average_lifespan = timedelta(days=27375)

    racial_class = racialclass.Bugbear
    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(strength=13, dexterity=9),
            maximum_set=abilityscores.AbilityScoreSet(charisma=15, intelligence=15),
        ),
        classes=restrictions.ClassRestrictionSet(
            included=(classes.Cleric, classes.Fighter, classes.Thief)
        ),
    )
    racial_language = languages.Bugbear
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.Darkvision,
    ))
