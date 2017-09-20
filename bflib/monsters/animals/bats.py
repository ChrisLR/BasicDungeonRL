from bflib import dice
import bflib.movement
from bflib import units
from bflib.attacks import AttackSet, Bite, ConfusionBySwarm
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.tables.attackbonus import AttackBonusTable


class Bat(Animal):
    name = "Bat"
    hit_dice = dice.D1(1)
    attack_bonus = AttackBonusTable.get_by_hit_dice(0)
    attack_sets = [AttackSet(ConfusionBySwarm(None))]
    base_armor_class = 14

    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(30), fly=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D100(1), dice_wild=dice.D100(2), dice_lair=dice.D100(2))
    save_as = None
    xp = 10


class GiantBat(Animal):
    name = "Giant Bat"
    hit_dice = dice.D8(2)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Bite(dice.D4(1)))]
    base_armor_class = 14

    morale = 8
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(10), fly=units.FeetPerGameTurn(60))
    no_appearing = AppearingSet(dice_dungeon=dice.D10(1), dice_wild=dice.D10(1), dice_lair=dice.D10(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    xp = 75
