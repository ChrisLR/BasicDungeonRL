from bflib import dice
import bflib.movement
from bflib import units
from bflib.attacks import AttackSet, Claw
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.tables.attackbonus import AttackBonusTable


class CarnivorousApe(Animal):
    name = "Carnivorous Ape"
    hit_dice = dice.D8(4)
    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Claw(dice.D4(1)), amount=2)]
    base_armor_class = 14

    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D6(1), dice_wild=dice.D4(2), dice_lair=dice.D4(2))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    xp = 240
