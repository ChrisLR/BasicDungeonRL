from bflib import dice
from bflib import restrictions
from bflib.characters import abilityscores
from bflib.characters import specialabilities
from bflib.characters.classes.level import Level, LevelTable
from bflib.characters.classes.base import CharacterClass
from bflib.characters.savingthrows import SavingThrowSet
from bflib.items import armor, weapons
from bflib.spells import SpellSlotSet


class MagicUser(CharacterClass):
    name = "Magic-User"
    restriction_set = restrictions.RestrictionSet(
        ability_score=restrictions.AbilityScoreRestrictionSet(
            minimum_set=abilityscores.AbilityScoreSet(intelligence=9)
        ),
        armor=restrictions.ArmorRestrictionSet(included=(armor.types.Clothing, ), shields=False),
        weapons=restrictions.WeaponRestrictionSet(
            included=(
                weapons.types.Dagger,
                weapons.types.Cudgel,
                weapons.types.WalkingStaff,
            )
        )
    )
    special_abilities = specialabilities.SpecialAbilitySet(
        special_abilities=(
            specialabilities.ArcaneCaster,
            specialabilities.ReadMagic
        )
    )
    level_table = LevelTable(
        levels=(
            Level(
                value=1,
                attack_bonus=1,
                experience_required=0,
                hit_dice=dice.D4(1),
                saving_throws_set=SavingThrowSet(
                    death_poison=13,
                    dragon_breath=16,
                    paralysis_stone=13,
                    spells=15,
                    wands=14
                ),
                spell_slots_set=SpellSlotSet(level_1=1)
            ),
            Level(
                value=2,
                attack_bonus=1,
                experience_required=2500,
                hit_dice=dice.D4(2),
                saving_throws_set=SavingThrowSet(
                    death_poison=13,
                    dragon_breath=15,
                    paralysis_stone=13,
                    spells=14,
                    wands=14
                ),
                spell_slots_set=SpellSlotSet(level_1=2)
            ),
            Level(
                value=3,
                attack_bonus=1,
                experience_required=5000,
                hit_dice=dice.D4(3),
                saving_throws_set=SavingThrowSet(
                    death_poison=13,
                    dragon_breath=15,
                    paralysis_stone=13,
                    spells=14,
                    wands=14
                ),
                spell_slots_set=SpellSlotSet(level_1=2, level_2=1)
            ),
            Level(
                value=4,
                attack_bonus=2,
                experience_required=10000,
                hit_dice=dice.D4(4),
                saving_throws_set=SavingThrowSet(
                    death_poison=12,
                    dragon_breath=15,
                    paralysis_stone=12,
                    spells=13,
                    wands=13
                ),
                spell_slots_set=SpellSlotSet(level_1=2, level_2=2)
            ),
            Level(
                value=5,
                attack_bonus=2,
                experience_required=20000,
                hit_dice=dice.D4(5),
                saving_throws_set=SavingThrowSet(
                    death_poison=12,
                    dragon_breath=15,
                    paralysis_stone=12,
                    spells=13,
                    wands=13
                ),
                spell_slots_set=SpellSlotSet(level_1=2, level_2=2, level_3=1)
            ),
            Level(
                value=6,
                attack_bonus=3,
                experience_required=40000,
                hit_dice=dice.D4(6),
                saving_throws_set=SavingThrowSet(
                    death_poison=12,
                    dragon_breath=14,
                    paralysis_stone=11,
                    spells=13,
                    wands=12
                ),
                spell_slots_set=SpellSlotSet(level_1=3, level_2=2, level_3=2)
            ),
            Level(
                value=7,
                attack_bonus=3,
                experience_required=80000,
                hit_dice=dice.D4(7),
                saving_throws_set=SavingThrowSet(
                    death_poison=12,
                    dragon_breath=14,
                    paralysis_stone=11,
                    spells=13,
                    wands=12
                ),
                spell_slots_set=SpellSlotSet(level_1=3, level_2=2, level_3=2, level_4=1)
            ),
            Level(
                value=8,
                attack_bonus=3,
                experience_required=150000,
                hit_dice=dice.D4(8),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=14,
                    paralysis_stone=10,
                    spells=12,
                    wands=11
                ),
                spell_slots_set=SpellSlotSet(level_1=3, level_2=3, level_3=2, level_4=2)
            ),
            Level(
                value=9,
                attack_bonus=4,
                experience_required=300000,
                hit_dice=dice.D4(9),
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=14,
                    paralysis_stone=10,
                    spells=12,
                    wands=11
                ),
                spell_slots_set=SpellSlotSet(level_1=3, level_2=3, level_3=2, level_4=2, level_5=1)
            ),
            Level(
                value=10,
                attack_bonus=4,
                experience_required=450000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=1,
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=13,
                    paralysis_stone=9,
                    spells=11,
                    wands=10
                ),
                spell_slots_set=SpellSlotSet(level_1=4, level_2=3, level_3=3, level_4=2, level_5=2)
            ),
            Level(
                value=11,
                attack_bonus=4,
                experience_required=600000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=2,
                saving_throws_set=SavingThrowSet(
                    death_poison=11,
                    dragon_breath=13,
                    paralysis_stone=9,
                    spells=11,
                    wands=10
                ),
                spell_slots_set=SpellSlotSet(level_1=4, level_2=4, level_3=3, level_4=2, level_5=2, level_6=1)
            ),
            Level(
                value=12,
                attack_bonus=4,
                experience_required=750000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=3,
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=13,
                    paralysis_stone=9,
                    spells=11,
                    wands=10
                ),
                spell_slots_set=SpellSlotSet(level_1=4, level_2=4, level_3=3, level_4=3, level_5=2, level_6=2)
            ),
            Level(
                value=13,
                attack_bonus=5,
                experience_required=900000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=4,
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=13,
                    paralysis_stone=9,
                    spells=11,
                    wands=10
                ),
                spell_slots_set=SpellSlotSet(level_1=4, level_2=4, level_3=4, level_4=3, level_5=2, level_6=2)
            ),
            Level(
                value=14,
                attack_bonus=5,
                experience_required=1050000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=5,
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=12,
                    paralysis_stone=8,
                    spells=10,
                    wands=9
                ),
                spell_slots_set=SpellSlotSet(level_1=4, level_2=4, level_3=4, level_4=3, level_5=3, level_6=2)
            ),
            Level(
                value=15,
                attack_bonus=5,
                experience_required=1200000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=6,
                saving_throws_set=SavingThrowSet(
                    death_poison=10,
                    dragon_breath=12,
                    paralysis_stone=8,
                    spells=10,
                    wands=9
                ),
                spell_slots_set=SpellSlotSet(level_1=5, level_2=4, level_3=4, level_4=3, level_5=3, level_6=2)
            ),
            Level(
                value=16,
                attack_bonus=6,
                experience_required=1350000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=7,
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=12,
                    paralysis_stone=7,
                    spells=9,
                    wands=8
                ),
                spell_slots_set=SpellSlotSet(level_1=5, level_2=5, level_3=4, level_4=3, level_5=3, level_6=2)
            ),
            Level(
                value=17,
                attack_bonus=6,
                experience_required=1500000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=8,
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=12,
                    paralysis_stone=7,
                    spells=9,
                    wands=8
                ),
                spell_slots_set=SpellSlotSet(level_1=5, level_2=5, level_3=4, level_4=4, level_5=3, level_6=3)
            ),
            Level(
                value=18,
                attack_bonus=6,
                experience_required=1650000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=9,
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=11,
                    paralysis_stone=6,
                    spells=9,
                    wands=7
                ),
                spell_slots_set=SpellSlotSet(level_1=6, level_2=5, level_3=4, level_4=4, level_5=3, level_6=3)
            ),
            Level(
                value=19,
                attack_bonus=7,
                experience_required=1800000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=10,
                saving_throws_set=SavingThrowSet(
                    death_poison=9,
                    dragon_breath=11,
                    paralysis_stone=6,
                    spells=9,
                    wands=7
                ),
                spell_slots_set=SpellSlotSet(level_1=6, level_2=5, level_3=5, level_4=4, level_5=3, level_6=3)
            ),
            Level(
                value=20,
                attack_bonus=7,
                experience_required=1950000,
                hit_dice=dice.D4(9),
                hit_dice_flat_bonus=11,
                saving_throws_set=SavingThrowSet(
                    death_poison=8,
                    dragon_breath=11,
                    paralysis_stone=5,
                    spells=8,
                    wands=6
                ),
                spell_slots_set=SpellSlotSet(level_1=6, level_2=5, level_3=5, level_4=4, level_5=4, level_6=3)
            )
        )
    )
