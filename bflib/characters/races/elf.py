from datetime import timedelta

from bflib import dice
from bflib import languages
from bflib import restrictions
from bflib import units
from bflib.characters import abilityscores, specialabilities, savingthrows
from bflib.characters.races.base import Race


class Elf(Race):
    name = "Elf"
    average_height = units.Feet(5)
    average_weight = units.Pound(130)
    average_lifespan = timedelta(days=438000)

    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(intelligence=9),
            maximum_set=abilityscores.AbilityScoreSet(constitution=17),
        ),
        classes=restrictions.ClassRestrictionSet(
            access_combined=True
        ),
        hit_dice_max_size=restrictions.HitDiceMaxSizeRestriction(dice.D6)
    )
    racial_language = languages.Elvish
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.Darkvision,
        specialabilities.DetectSecretDoor,
        specialabilities.GhoulParalysisImmunity,
        specialabilities.SurpriseResistance
    ))
    saving_throw_set = savingthrows.SavingThrowSet(
        paralysis_stone=1,
        spells=2,
        wands=2
    )
