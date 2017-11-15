from bflib import dice, movement, units
from bflib.attacks import AttackSet, Bite, Gaze
from bflib.attacks import specialproperties
from bflib.characters import specialabilities
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.reptilians.base import Reptilian
from bflib.sizes import Size
from bflib.tables.attackbonus import AttackBonusTable
from bflib.treasuretypes import TreasureType


@listing.register_type
@listing.register_monster
class Basilisk(Reptilian):
    name = "Basilisk"
    hit_dice = dice.D8(6)

    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    attack_sets = [AttackSet(Bite(dice.D10(1))), AttackSet(Gaze(None), special_properties=specialproperties.Petrify)]
    base_armor_class = 16
    morale = 9
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(20), turning_distance=units.Feet(10))
    no_appearing = AppearingSet(dice_dungeon=dice.D6(1), dice_wild=dice.D6(1), dice_lair=dice.D6(1))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Large
    special_abilities = specialabilities.CombatFrenzy,
    treasure_type = TreasureType.F
    weight = units.Pound(300)
    xp = 610
