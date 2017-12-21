from bflib import dice, movement, units
from bflib.characters import specialabilities
from bflib.characters.classes.fighter import Fighter
from bflib.monsters import listing
from bflib.monsters.appearingset import AppearingSet
from bflib.monsters.undeads.base import Undead
from bflib.sizes import Size
from bflib.tables.attackbonus import AttackBonusTable


@listing.register_type
@listing.register_monster
class Skeleton(Undead):
    name = "Skeleton"
    hit_dice = dice.D8(1)

    attack_bonus = AttackBonusTable.get_by_hit_dice(hit_dice.amount)
    base_armor_class = 13
    morale = 12
    movement = movement.MovementSet(walk=units.FeetPerGameTurn(40))
    no_appearing = AppearingSet(dice_dungeon=dice.D6(3), dice_wild=dice.D10(3))
    save_as = Fighter.level_table.levels[hit_dice.amount].saving_throws_set
    size = Size.Medium
    special_abilities = (
        specialabilities.EdgedWeaponResistance,
        specialabilities.ProjectileResistance,
        specialabilities.SleepImmunity,
        specialabilities.CharmImmunity,
        specialabilities.HoldImmunity,
        specialabilities.Mindless
    )
    treasure_type = None
    weight = units.Pound(100)
    xp = 25
