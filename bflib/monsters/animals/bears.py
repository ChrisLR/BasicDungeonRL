from bflib import dice
import bflib.movement
from bflib import units
from bflib.attacks import AttackChain, AttackSet, Bite, Claw, Crush
from bflib.attacks import specialproperties
from bflib.characters.classes.fighter import Fighter
from bflib.characters.specialabilities import LastBreath
from bflib.characters.specialabilities.set import SpecialAbilitySet
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.tables.attackbonus import AttackBonusTable


class BlackBear(Animal):
    name = "Black Bear"
    hit_dice = dice.D8(4)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [
        AttackChain(
            AttackSet(Claw(dice.D4(1)), amount=2, special_properties=specialproperties.BearHug),
            AttackSet(Bite(dice.D6(1)))
        ),
        AttackSet(Crush(dice.D6(2)))
    ]
    base_armor_class = 14

    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D4(1), dice_wild=dice.D4(1), dice_lair=dice.D4(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = SpecialAbilitySet((LastBreath,))
    xp = 240


class CaveBear(Animal):
    name = "Cave Bear"
    hit_dice = dice.D8(7)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [
        AttackChain(
            AttackSet(Claw(dice.D8(1)), amount=2, special_properties=specialproperties.BearHug),
            AttackSet(Bite(dice.D6(2)))
        ),
        AttackSet(Crush(dice.D8(2)))
    ]
    base_armor_class = 15

    morale = 9
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D2(1), dice_wild=dice.D2(1), dice_lair=dice.D2(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = SpecialAbilitySet((LastBreath,))
    xp = 670


class GrizzlyBear(Animal):
    name = "Grizzly Bear"
    hit_dice = dice.D8(5)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [
        AttackChain(
            AttackSet(Claw(dice.D4(1)), amount=2, special_properties=specialproperties.BearHug),
            AttackSet(Bite(dice.D8(1)))
        ),
        AttackSet(Crush(dice.D8(2)))
    ]
    base_armor_class = 14

    morale = 8
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D1(1), dice_wild=dice.D4(1), dice_lair=dice.D4(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = SpecialAbilitySet((LastBreath,))
    xp = 360


class PolarBear(Animal):
    name = "Polar Bear"
    hit_dice = dice.D8(6)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [
        AttackChain(
            AttackSet(Claw(dice.D6(1)), amount=2, special_properties=specialproperties.BearHug),
            AttackSet(Bite(dice.D10(1)))
        ),
        AttackSet(Crush(dice.D8(2)))
    ]
    base_armor_class = 14

    morale = 8
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D1(1), dice_wild=dice.D2(1), dice_lair=dice.D2(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = SpecialAbilitySet((LastBreath,))
    xp = 500
