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
    target_type = targettypes.Touch


class FallingStone(Trap):
    name = "Falling Stone Trap"
    attack = Attack(dice.D10(1, flat_bonus=1))
    saving_throw = savingthrows.ParalysisStone
    target_type = targettypes.Touch


class FlashingLight(Trap):
    name = "Flashing Light Trap"
    effect = effects.Blind
    saving_throw = savingthrows.Spells


class MonsterAttractingSpray(Trap):
    name = "Monster Attracting Spray Trap"
    effect = effects.StrongSmell
    target_type = targettypes.Touch


class OilSlick(Trap):
    name = "Oil Slick Trap"
    saving_throw = savingthrows.DeathPoison


class Pit(Trap):
    name = "Pit Trap"
    saving_throw = savingthrows.DeathPoison


class PoisonDart(Trap):
    name = "Poison Dart Trap"
    attack = WeaponAttack(dice.D4(1))
    attack_bonus = 1
    effect = effects.FatalPoison
    saving_throw = savingthrows.DeathPoison
    target_type = targettypes.Touch


class PoisonGas(Trap):
    name = "Poison Gas Trap"
    effect = effects.FatalPoison
    saving_throw = savingthrows.DeathPoison
    target_type = targettypes.Room


class PoisonNeedle(Trap):
    name = "Poison Needle Trap"
    effect = effects.FatalPoison
    saving_throw = savingthrows.DeathPoison
    target_type = targettypes.Touch


class Portcullis(Trap):
    name = "Portcullis Trap"
    attack = Attack(dice.D6(3))
    saving_throw = savingthrows.DeathPoison
    target_type = targettypes.Touch


class RollingBoulder(Trap):
    name = "Rolling Boulder Trap"
    attack = Attack(dice.D6(2))
    saving_throw = savingthrows.DeathPoison
    target_type = targettypes.AreaOfEffect(Shape.Line, units.Feet(1000))


class TriggeredSpell(Trap):
    name = "Triggered Spell Trap"
