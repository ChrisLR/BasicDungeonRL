from bflib import dice
from bflib import movement
from bflib import units
from bflib.characters.classes.fighter import Fighter
from bflib.characters.specialabilities import Darkvision
from bflib.characters.specialabilities.set import SpecialAbilitySet
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.humanoids.base import Humanoid
from bflib.tables.attackbonus import AttackBonusTable


class Goblin(Humanoid):
    name = "Goblin"
    hit_dice = dice.D1(1)
    attack_bonus = AttackBonusTable.get_by_hit_dice(1)
    attack_sets = None
    base_armor_class = 14

    morale = 7
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(30))
    no_appearing = AppearingSet(dice_dungeon=dice.D4(2), dice_wild=dice.D10(6), dice_lair=dice.D10(6))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    special_abilities = SpecialAbilitySet((Darkvision,))
    xp = 10