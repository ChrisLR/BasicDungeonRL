from bflib import dice
import bflib.movement
from bflib import units
from bflib.attacks import AttackChain, AttackSet, Bite, Hoof
from bflib.carrycapacity import CarryCapacity
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.tables.attackbonus import AttackBonusTable


class Camel(Animal):
    name = "Camel"
    attack_bonus = AttackBonusTable.get_by_hit_dice(2)
    attack_sets = [AttackChain(AttackSet(Bite(dice.D1(1))), AttackSet(Hoof(dice.D4(1))))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(400), units.Pound(800))
    hit_dice = dice.D8(2)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(50), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D4(2))
    save_as = Fighter.level_table.levels[2].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 75


class Donkey(Animal):
    name = "Donkey"
    attack_bonus = AttackBonusTable.get_by_hit_dice(2)
    attack_sets = [AttackSet(Bite(dice.D2(1)))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(400), units.Pound(800))
    hit_dice = dice.D8(2)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D4(2))
    save_as = Fighter.level_table.levels[2].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 75


class DraftHorse(Animal):
    name = "Draft Horse"
    attack_bonus = AttackBonusTable.get_by_hit_dice(3)
    attack_sets = [AttackSet(Hoof(dice.D4(1)), amount=2)]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(350), units.Pound(700))
    hit_dice = dice.D8(3)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(60), turning_distance=units.Feet(10))
    no_appearing = None
    save_as = Fighter.level_table.levels[3].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 145


class Mule(Animal):
    name = "Mule"
    attack_bonus = AttackBonusTable.get_by_hit_dice(2)
    attack_sets = [AttackSet(Hoof(dice.D4(1))), AttackSet(Bite(dice.D2(1)))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(300), units.Pound(600))
    hit_dice = dice.D8(2)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40), turning_distance=units.Feet(10))
    no_appearing = None
    save_as = Fighter.level_table.levels[2].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 75


class Pony(Animal):
    name = "Pony"
    attack_bonus = AttackBonusTable.get_by_hit_dice(1)
    attack_sets = [AttackSet(Bite(dice.D4(1)))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(275), units.Pound(550))
    hit_dice = dice.D8(2)
    morale = 6
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40), turning_distance=units.Feet(10))
    no_appearing = None
    save_as = Fighter.level_table.levels[1].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 25


class RidingHorse(Animal):
    name = "Riding Horse"
    attack_bonus = AttackBonusTable.get_by_hit_dice(2)
    attack_sets = [AttackSet(Hoof(dice.D4(1)), amount=2)]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(250), units.Pound(500))
    hit_dice = dice.D8(2)
    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(10))
    save_as = Fighter.level_table.levels[2].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 75


class WarHorse(Animal):
    name = "War Horse"
    attack_bonus = AttackBonusTable.get_by_hit_dice(3)
    attack_sets = [AttackSet(Hoof(dice.D6(1)), amount=2)]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(250), units.Pound(500))
    hit_dice = dice.D8(3)
    morale = 9
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(60), turning_distance=units.Feet(10))
    no_appearing = None
    save_as = Fighter.level_table.levels[3].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 145


class WarPony(Animal):
    name = "War Pony"
    attack_bonus = AttackBonusTable.get_by_hit_dice(1)
    attack_sets = [AttackSet(Bite(dice.D4(1)))]
    base_armor_class = 13
    carry_capacity = CarryCapacity(units.Pound(275), units.Pound(550))
    hit_dice = dice.D8(2)
    morale = 9
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40), turning_distance=units.Feet(10))
    no_appearing = None
    save_as = Fighter.level_table.levels[1].saving_throws_set
    special_abilities = None
    treasure_type = None
    xp = 25
