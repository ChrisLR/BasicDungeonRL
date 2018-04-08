from bflib import attacks
from bflib.characters import specialabilities
from core import contexts, events
from core.attacks import listing
from core.attacks.base import MeleeAttack
from messaging import StringBuilder, Attacker, Defender, Verb, His


class NaturalAttack(MeleeAttack):
    name = ""
    on_success = StringBuilder(Attacker, Verb("hit", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "attack,")

    def can_execute(self, attacker, defender):
        # Natural attacks should come from the body, in turn it should check for it when used.
        return True

    def echo(self, attacker, defender, success, damage, sneak_attack=False):
        context = contexts.Combat(attacker, defender)
        if success:
            if sneak_attack:
                message = self.on_stealth + "for {} damage!".format(damage)
            else:
                message = self.on_success + "for {} damage!".format(damage)
        else:
            message = self.on_failure
        self.game.echo.see(attacker, message, context)

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
    name = "bite"
    base_attack = attacks.Bite
    on_success = StringBuilder(Attacker, Verb("bite", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "bite,")


@listing.register
class Claw(NaturalAttack):
    name = "claw"
    base_attack = attacks.Claw
    on_success = StringBuilder(Attacker, Verb("claw", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "claw,")


@listing.register
class Crush(NaturalAttack):
    name = "crush"
    base_attack = attacks.Crush
    on_success = StringBuilder(Attacker, Verb("crush", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "crushing attack,")


@listing.register
class ConfusionBySwarm(NaturalAttack):
    name = "Confusion By Swarm"
    base_attack = attacks.ConfusionBySwarm
    on_success = StringBuilder(Attacker, Verb("confuse", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "confusing attack,")


@listing.register
class Gaze(NaturalAttack):
    name = "gaze"
    base_attack = attacks.Gaze
    on_success = StringBuilder(Attacker, Verb("gaze", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "gaze,")


@listing.register
class Headbutt(NaturalAttack):
    name = "headbutt"
    base_attack = attacks.Headbutt
    on_success = StringBuilder(Attacker, Verb("headbutt", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "headbutt,")


@listing.register
class Hoof(NaturalAttack):
    name = "hoof"
    base_attack = attacks.Hoof
    on_success = StringBuilder(Attacker, Verb("hoof", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "hoof,")


@listing.register
class Sting(NaturalAttack):
    name = "sting"
    base_attack = attacks.Sting
    on_success = StringBuilder(Attacker, Verb("sting", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "sting,")


@listing.register
class Punch(NaturalAttack):
    name = "punch"
    base_attack = attacks.Punch
    on_success = StringBuilder(Attacker, Verb("punch", Attacker), Defender)
    on_failure = StringBuilder(Defender, Verb("dodge", Defender), His(Attacker), "attack!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "punch,")

