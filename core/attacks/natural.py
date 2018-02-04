from bflib import attacks
from core.attacks.base import MeleeAttack
from services.echo import functions as echo_functions
from services.echo.service import echo_service
from core.attacks import listing


class NaturalAttack(MeleeAttack):
    actor_on_success = "You attack {defender} for {damage} damage."
    actor_on_failure = "{defender} dodges your attack"
    observer_on_success = "{attacker} attacks {defender} for {damage} damage."
    observer_on_failure = "{defender} dodge {attacker} attack"

    @classmethod
    def can_execute(cls, attacker, defender):
        return True

    @classmethod
    def echo(cls, attacker, defender, success, damage):
        if echo_functions.is_player(attacker):
            if success:
                echo_service.echo(
                    cls.actor_on_success.format(
                        defender=echo_functions.name_or_you(defender).capitalize(),
                        damage=damage
                    )
                )
            else:
                echo_service.echo(
                    cls.actor_on_failure.format(
                        defender=echo_functions.name_or_you(defender).capitalize()
                    )
                )
        else:
            if success:
                echo_service.echo(
                    cls.observer_on_success.format(
                        attacker=echo_functions.name_or_you(attacker).capitalize(),
                        defender=echo_functions.name_or_you(defender).capitalize(),
                        damage=damage
                    )
                )
            else:
                echo_service.echo(
                    cls.observer_on_failure.format(
                        attacker=echo_functions.names_or_your(attacker).capitalize(),
                        defender=echo_functions.name_or_you(defender).capitalize()
                    )
                )

    @classmethod
    def execute(cls, attacker, defender, attack_set):
        hits = 0
        for _ in range(0, attack_set.amount):
            success = cls.make_melee_hit_roll(attacker, defender)
            if success:
                hits += 1
                base_attack = attack_set.attack
                damage = cls.make_melee_damage_roll(
                    attacker, base_attack.damage_dice,
                    base_attack.damage_bonus
                )

                cls.echo(attacker, defender, True, damage)
                defender.health.take_damage(damage, attacker)
            else:
                cls.echo(attacker, defender, False, 0)

        return True


@listing.register
class Bite(NaturalAttack):
    base_attack = attacks.Bite


@listing.register
class Claw(NaturalAttack):
    base_attack = attacks.Claw


@listing.register
class Crush(NaturalAttack):
    base_attack = attacks.Crush


@listing.register
class ConfusionBySwarm(NaturalAttack):
    base_attack = attacks.ConfusionBySwarm


@listing.register
class Gaze(NaturalAttack):
    base_attack = attacks.Gaze


@listing.register
class Headbutt(NaturalAttack):
    base_attack = attacks.Headbutt


@listing.register
class Hoof(NaturalAttack):
    base_attack = attacks.Hoof


@listing.register
class Sting(NaturalAttack):
    base_attack = attacks.Sting


@listing.register
class Punch(NaturalAttack):
    base_attack = attacks.Punch
