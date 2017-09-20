from bflib import dice
import bflib.movement
from bflib import units
from bflib.attacks import AttackSet, Headbutt
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.tables.attackbonus import AttackBonusTable


class Auroch(Animal):
    name = "Auroch"
    hit_dice = dice.D8(2)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D6(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    xp = 75


class Bison(Animal):
    name = "Bison"
    hit_dice = dice.D8(4)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D8(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    xp = 240


class Deer(Animal):
    name = "Deer"
    hit_dice = dice.D8(1)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D4(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    xp = 25


class Moose(Animal):
    name = "Moose"
    hit_dice = dice.D8(3)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D6(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    xp = 145
