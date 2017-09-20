from datetime import timedelta

from bflib import dice
from bflib import languages
from bflib import restrictions
from bflib import units
from bflib.characters import abilityscores, classes, specialabilities, savingthrows
from bflib.characters.races.base import Race


class Halfling(Race):
    name = "Halfling"
    average_height = units.Feet(3)
    average_weight = units.Pound(60)
    average_lifespan = timedelta(days=109500)

    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(dexterity=9),
            maximum_set=abilityscores.AbilityScoreSet(strength=17),
        ),
        classes=restrictions.ClassRestrictionSet(
            included=(classes.Cleric, classes.Fighter, classes.Thief),
        ),
        hit_dice_max_size=restrictions.HitDiceMaxSizeRestriction(dice.D6),
        weapon_size=restrictions.WeaponSizeRestrictionSet(
            large=restrictions.WeaponSizeRestrictionSet.keywords.CannotWield,
            medium=restrictions.WeaponSizeRestrictionSet.keywords.NeedsTwoHands,
            small=restrictions.WeaponSizeRestrictionSet.keywords.CanWield,
        )
    )
    racial_language = languages.Halfling
    special_ability_set = specialabilities.SpecialAbilitySet((
        specialabilities.HalflingHide,
        specialabilities.InitiativeBonus(1),
        specialabilities.MeleeDefenseBonus(2),
        specialabilities.RangedWeaponAccuracyBonus(1)
    ))
    saving_throw_set = savingthrows.SavingThrowSet(
        death_poison=4,
        dragon_breath=3,
        paralysis_stone=4,
        spells=4,
        wands=4
    )
