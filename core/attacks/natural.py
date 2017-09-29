from bflib import attacks
from core.attacks.base import MeleeAttack


class NaturalAttack(MeleeAttack):
    @classmethod
    def can_execute(cls, attacker, defender):
        return True

    @classmethod
    def execute(cls, attacker, defender, attack_set):
        hits = 0
        for _ in range(0, attack_set):
            success = cls.make_melee_hit_roll(attacker, defender)
            if success:
                hits += 1
                base_attack = attack_set.attack
                damage = cls.make_melee_damage_roll(
                    attacker, base_attack.damage_dice,
                    base_attack.damage_bonus
                )
                defender.health.take_damage(damage)

        return True


class Bite(NaturalAttack):
    base_attack = attacks.Bite


class Claw(NaturalAttack):
    base_attack = attacks.Claw


class Crush(NaturalAttack):
    base_attack = attacks.Crush


class ConfusionBySwarm(NaturalAttack):
    base_attack = attacks.ConfusionBySwarm


class Gaze(NaturalAttack):
    base_attack = attacks.Gaze


class Headbutt(NaturalAttack):
    base_attack = attacks.Headbutt


class Hoof(NaturalAttack):
    base_attack = attacks.Hoof


class Sting(NaturalAttack):
    base_attack = attacks.Sting
