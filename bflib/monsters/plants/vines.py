import dice
import movement
import units
from bflib.attacks import AttackSet, Crush
from bflib.characters import specialabilities
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.plants.base import Plant
from bflib.tables.attackbonus import AttackBonusTable
from bflib.treasuretypes import TreasureType
from bflib.attacks.specialproperties import CrushingEntanglement


class AssassinVine(Plant):
    name = "Assassin Vine"
    hit_dice = dice.D8(6)

    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Crush(dice.D8(1)), special_properties=(CrushingEntanglement, ))]
    base_armor_class = 15
    morale = 12
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(5))
    no_appearing = AppearingSet(dice_dungeon=dice.D4(1, 1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    treasure_type = TreasureType.U
    xp = 500
