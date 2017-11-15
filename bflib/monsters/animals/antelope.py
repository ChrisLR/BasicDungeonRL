from bflib import dice, movement, units
from bflib.attacks import AttackSet, Headbutt
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.sizes import Size
from bflib.tables.attackbonus import AttackBonusTable


@listing.register_type
class Antelope(Animal):
    pass


@listing.register_monster
class Auroch(Antelope):
    name = "Auroch"
    hit_dice = dice.D8(2)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D6(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Large
    weight = units.Pound(1000)
    xp = 75


@listing.register_monster
class Bison(Antelope):
    name = "Bison"
    hit_dice = dice.D8(4)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D8(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Large
    weight = units.Pound(1366)
    xp = 240


@listing.register_monster
class Deer(Antelope):
    name = "Deer"
    hit_dice = dice.D8(1)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D4(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Medium
    weight = units.Pound(220)
    xp = 25


@listing.register_monster
class Moose(Antelope):
    name = "Moose"
    hit_dice = dice.D8(3)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Headbutt(dice.D6(1)))]
    base_armor_class = 13

    morale = 5
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(80), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Large
    weight = units.Pound(1190)
    xp = 145
