from bflib import dice
from bflib import restrictions
from bflib.characters import specialabilities
from bflib.characters.classes.base import CharacterClass
from bflib.characters.classes.fighter import Fighter
from bflib.characters.classes.level import Level, LevelTable
from bflib.characters.specialabilities.set import SpecialAbilitySet
from bflib.items.armor.lightarmor import LeatherArmor


class Bugbear(CharacterClass):
    name = "Bugbear"
    restriction_set = restrictions.RestrictionSet(
        armor=restrictions.ArmorRestrictionSet(included=(LeatherArmor,))
    )
    level_table = LevelTable(
        levels=(
            Level(
                value=1,
                attack_bonus=1,
                experience_required=-3000,
                hit_dice=dice.D8(1),
                saving_throws_set=Fighter.level_table.get(1).saving_throws_set,
            ),
            Level(
                value=2,
                attack_bonus=2,
                experience_required=-1500,
                hit_dice=dice.D8(2),
                saving_throws_set=Fighter.level_table.get(1).saving_throws_set
            ),
            Level(
                value=3,
                attack_bonus=2,
                experience_required=0,
                hit_dice=dice.D8(2),
                saving_throws_set=Fighter.level_table.get(1).saving_throws_set,
                special_ability_set=SpecialAbilitySet((
                    specialabilities.BugBearStealth,
                    specialabilities.MoveSilently(20),
                    specialabilities.Hide(10))
                ),
            )
        )
    )
