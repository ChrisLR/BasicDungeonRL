from bflib import dice, movement, units
from bflib.attacks import AttackSet, Bite, specialproperties
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.animals.base import Animal
from bflib.monsters.appearingset import AppearingSet
from bflib.sizes import Size
from bflib.tables.attackbonus import AttackBonusTable


@listing.register_type
class Arachnid(Animal):
    pass


@listing.register_monster
class GiantBlackWidow(Arachnid):
    name = "Giant Black Widow"
    hit_dice = dice.D8(3)
    attack_bonus = AttackBonusTable.get_by_hit_dice(0)
    attack_sets = [AttackSet(Bite(dice.D6(2)), special_properties=specialproperties.DeathPoison)]
    base_armor_class = 14

    morale = 8
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(20))
    no_appearing = AppearingSet(dice_dungeon=dice.D4(1), dice_wild=dice.D4(1), dice_lair=dice.D4(1))
    save_as = None
    size = Size.Medium
    weight = units.Pound(200)
    xp = 175
