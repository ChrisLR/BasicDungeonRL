from bflib import dice, movement, units
from bflib.attacks import AttackSet, Crush
from bflib.attacks.specialproperties import CrushingEntanglement
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.plants.base import Plant
from bflib.sizes import Size
from bflib.tables.attackbonus import AttackBonusTable
from bflib.treasuretypes import TreasureType


@listing.register_type
class Vine(Plant):
    pass


@listing.register_monster
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
    size = Size.Small
    treasure_type = TreasureType.U
    weight = units.Pound(15)
    xp = 500
