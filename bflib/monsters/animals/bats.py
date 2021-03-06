from bflib import dice, movement, units
from bflib.attacks import AttackSet, Bite, ConfusionBySwarm
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.sizes import Size
from bflib.tables.attackbonus import AttackBonusTable


@listing.register_type
@listing.register_monster
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
    size = Size.VerySmall
    weight = units.Pound(200)
    xp = 10


@listing.register_monster
class GiantBat(Bat):
    name = "Giant Bat"
    hit_dice = dice.D8(2)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Bite(dice.D4(1)))]
    base_armor_class = 14

    morale = 8
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(10), fly=units.FeetPerGameTurn(60))
    no_appearing = AppearingSet(dice_dungeon=dice.D10(1), dice_wild=dice.D10(1), dice_lair=dice.D10(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Large
    weight = units.Pound(200)
    xp = 75
