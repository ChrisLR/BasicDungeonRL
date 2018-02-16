from datetime import timedelta

from bflib import languages, restrictions, units
from bflib.characters import abilityscores, classes, specialabilities, \
    racialclass, savingthrows
from bflib.characters.races.base import Race


class Gnoll(Race):
    name = "Gnoll"
    average_height = units.Feet(7)
    average_weight = units.Pound(300)
    average_lifespan = timedelta(days=27375)

    racial_class = racialclass.Gnoll
    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(strength=13, constitution=11),
            maximum_set=abilityscores.AbilityScoreSet(charisma=15, intelligence=15),
        ),
        classes=restrictions.ClassRestrictionSet(
            included=(classes.Cleric, classes.Fighter, classes.MagicUser)
        ),
    )
    racial_language = languages.Bugbear
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.Darkvision,
        specialabilities.PowerfulScent,
    ))
    saving_throw_set = savingthrows.SavingThrowSet(
        death_poison=-4,
        paralysis_stone=-4,
    )
