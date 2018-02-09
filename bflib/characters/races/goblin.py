from datetime import timedelta

import bflib.items.weapons.ranged.bows
from bflib import languages, restrictions, units
from bflib.characters import abilityscores, specialabilities, savingthrows
from bflib.characters.races.base import Race


class Goblin(Race):
    name = "Goblin"
    average_height = units.Feet(3)
    average_weight = units.Pound(45)
    average_lifespan = timedelta(days=18250)

    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(dexterity=9),
            maximum_set=abilityscores.AbilityScoreSet(
                strength=16, constitution=16),
        ),
        weapons=restrictions.WeaponRestrictionSet(
            excluded=(
                bflib.items.weapons.melee.swords.TwoHandedSword,
                bflib.items.weapons.melee.polearms.Polearm,
                bflib.items.weapons.ranged.bows.Longbow,
            )
        )
    )
    racial_language = languages.Goblin
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.Darkvision,
        specialabilities.FeebleConstitution(1),
        specialabilities.MeleeDefenseBonus(2),
        specialabilities.DetectNewConstructions,
        specialabilities.DetectSecretDoor,
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
