from datetime import timedelta

import bflib.items.weapons.ranged.bows
from bflib import languages, restrictions, units
from bflib.characters import abilityscores, specialabilities
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
        weapon_size=restrictions.WeaponSizeRestrictionSet(
            large=restrictions.WeaponSizeRestrictionSet.keywords.CannotWield,
            medium=restrictions.WeaponSizeRestrictionSet.keywords.NeedsTwoHands,
            small=restrictions.WeaponSizeRestrictionSet.keywords.CanWield,
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
        specialabilities.OpenLock(10),
        specialabilities.RemoveTraps(10),
    ))
