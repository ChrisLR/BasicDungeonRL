from bflib import dice
import bflib.movement
from bflib import units
from bflib.attacks import AttackSet, Bite
from bflib.characters import specialabilities
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.insects.base import Insect
from bflib.tables.attackbonus import AttackBonusTable
from bflib.treasuretypes import TreasureType


class GiantAnt(Insect):
    name = "Giant Ant"
    hit_dice = dice.D8(4)

    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Bite(dice.D6(2)))]
    base_armor_class = 17
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(60), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_dungeon=dice.D6(2), dice_wild=dice.D6(2), dice_lair=dice.D6(4))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = specialabilities.CombatFrenzy,
    treasure_type = TreasureType.U
    xp = 25
