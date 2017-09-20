from datetime import timedelta

from bflib import languages
from bflib import restrictions
from bflib import units
from bflib.characters import abilityscores, classes, specialabilities, savingthrows
from bflib.characters.races.base import Race
from bflib.items import weapons


class Dwarf(Race):
    name = "Dwarf"
    average_height = units.Feet(4)
    average_weight = units.Pound(120)
    average_lifespan = timedelta(days=36500)

    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(constitution=9),
            maximum_set=abilityscores.AbilityScoreSet(charisma=17),
        ),
        classes=restrictions.ClassRestrictionSet(
            included=(classes.Cleric, classes.Fighter, classes.Thief)
        ),
        weapons=restrictions.WeaponRestrictionSet(
            excluded=(
                weapons.types.TwoHandedSword,
                weapons.types.Polearm,
                weapons.types.Longbow,
            )
        )
    )
    racial_language = languages.Dwarvish
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.Darkvision,
        specialabilities.DetectNewConstructions,
        specialabilities.DetectShiftingWalls,
        specialabilities.DetectSlantingPassages,
        specialabilities.DetectTraps,
    ))
    saving_throw_set = savingthrows.SavingThrowSet(
        death_poison=4,
        dragon_breath=3,
        paralysis_stone=4,
        spells=4,
        wands=4
    )
