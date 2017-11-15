from bflib import dice, movement, units
from bflib.attacks import AttackSet, Sting
from bflib.attacks import specialproperties
from bflib.characters import specialabilities
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.insects.base import Insect
from bflib.tables.attackbonus import AttackBonusTable
from bflib.treasuretypes import TreasureType


@listing.register_type
class Bee(Insect):
    pass


@listing.register_monster
class GiantBee(Bee):
    name = "Giant Bee"
    hit_dice = dice.D4(1)

    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Sting(dice.D4(1)), special_properties=specialproperties.DeathPoison)]
    base_armor_class = 13
    morale = 9
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(10), fly=units.Feet(50))
    no_appearing = AppearingSet(dice_dungeon=dice.D6(1), dice_wild=dice.D6(1), dice_lair=dice.D6(5))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = specialabilities.CombatFrenzy,
    treasure_type = TreasureType.Special
    xp = 13
