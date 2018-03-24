from bflib import attacks
from bflib.characters import specialabilities
from core.attacks import listing
from core.attacks.base import MeleeAttack
from core import events
from messaging import StringBuilder, Attacker, Defender, Verb, His


class NaturalAttack(MeleeAttack):
    on_success = StringBuilder(Attacker, Verb("hit", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), Attacker, "'s attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "attack!")

    def can_execute(self, attacker, defender):
        return True

    def echo(self, attacker, defender, success, damage, sneak_attack=False):
        
        if success:
            if sneak_attack:
                message = self.on_stealth
            else:
                message = self.on_success + "for {} damage!".format(damage)
        else:
            message = self.on_failure
        self.game.echo.player(message, context)

    def execute(self, attacker, defender, attack_set):
        sneak_attack = False
        if attacker.query.special_ability(specialabilities.SneakAttack):
            if not defender.vision.can_see_object(attacker):
                sneak_attack = True

        attacker.events.transmit(events.Attacking(attacker))
        hits = 0
        for _ in range(0, attack_set.amount):
            success = self.make_melee_hit_roll(attacker, defender, sneak_attack=sneak_attack)
            if success:
                hits += 1
                base_attack = attack_set.attack
                damage = self.make_melee_damage_roll(
                    attacker, base_attack.damage_dice,
                    base_attack.damage_bonus,
                    sneak_attack=sneak_attack
                )

                self.echo(attacker, defender, True, damage, sneak_attack=sneak_attack)
                defender.health.take_damage(damage, attacker)
            else:
                self.echo(attacker, defender, False, 0)

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
