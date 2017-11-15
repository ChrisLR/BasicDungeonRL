from bflib import dice, movement, units
from bflib.carrycapacity import CarryCapacity
from bflib.characters import specialabilities
from bflib.characters.classes.fighter import Fighter
from bflib.monsters.appearingset import AppearingSet
from bflib.sizes import Size
from bflib.treasuretypes import TreasureType


class Monster(object):
    name = ""
    attack_bonus = 0
    attack_sets = []
    base_armor_class = 0
    carry_capacity = CarryCapacity
    hit_dice = dice.Dice
    morale = 0
    movement = movement.MovementSet
    no_appearing = AppearingSet
    save_as = Fighter.level_table.levels[1].saving_throws_set
    size = Size
    special_abilities = specialabilities.SpecialAbilitySet
    treasure_type = TreasureType
    weight = units.Pound
    xp = 0
