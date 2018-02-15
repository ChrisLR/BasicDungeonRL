from bflib.traps.base import Trap
from bflib import dice, effects, shapes, targettypes, units
from bflib.attacks.base import Attack, WeaponAttack
from bflib.characters import savingthrows
from bflib.shapes import Shape


class Alarm(Trap):
    name = "Alarm Trap"

    effect = effects.Deaf
    saving_throw = savingthrows.Spells
    target_type = targettypes.AreaOfEffect(Shape.Circle, units.Feet(30))


class Arrow(Trap):
    name = "Arrow Trap"

    attack = WeaponAttack(dice.D6(1, flat_bonus=1))
    attack_bonus = 1
    target_type = targettypes.Touch


class Blade(Trap):
    name = "Blade Trap"

    attack = WeaponAttack(dice.D8(1, flat_bonus=1))
    attack_bonus = 1
    target_type = targettypes.AreaOfEffect(Shape.Line, units.Feet(10))


class Chute(Trap):
    name = "Chute Trap"

    saving_throw = savingthrows.DeathPoison


class FallingStone(Trap):
    name = "Falling Stone Trap"

    attack = Attack(dice.D10(1, flat_bonus=1))
    saving_throw = savingthrows.ParalysisStone


class FlashingLight(Trap):
    name = "Flashing Light Trap"


class MonsterAttractingSpray(Trap):
    name = "Monster Attracting Spray Trap"


class OilSlick(Trap):
    name = "Oil Slick Trap"


class Pit(Trap):
    name = "Pit Trap"


class PoisonDart(Trap):
    name = "Poison Dart Trap"


class PoisonGas(Trap):
    name = "Poison Gas Trap"


class PoisonNeedle(Trap):
    name = "Poison Needle Trap"


class Portcullis(Trap):
    name = "Portcullis Trap"


class RollingBoulder(Trap):
    name = "Rolling Boulder Trap"


class TriggeredSpell(Trap):
    name = "Triggered Spell Trap"
