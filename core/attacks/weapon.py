from bflib import attacks
from bflib.characters import specialabilities
from bflib.dice import D4
from core import contexts, events
from core.attacks import listing
from core.attacks.base import MeleeAttack
from messaging import StringBuilder, Attacker, Defender, Verb, His, AttackerWeapon


@listing.register
class WeaponAttack(MeleeAttack):
    base_attack = attacks.WeaponAttack
    on_success = StringBuilder(Attacker, Verb("hit", Attacker), Defender, "with", His(Attacker), AttackerWeapon)
    on_failure = StringBuilder(Attacker, Verb("miss", Attacker), Defender, "!")
    on_stealth = StringBuilder(Attacker, Verb("surprise", Attacker), Defender, "with", His(Attacker), "attack,")

    def can_execute(self, attacker, defender):
        if attacker.equipment.wielded_items:
            return True
        return False

    def execute(self, attacker, defender, attack_set):
        sneak_attack = False
        sorted_melee_weapons = self._sort_melee_weapons_by_damage(attacker)
        if attacker.query.special_ability(specialabilities.SneakAttack):
            if not defender.vision.can_see_object(attacker):
                sneak_attack = True

        attacker.events.transmit(events.Attacking(attacker))
        for _ in range(1, attack_set.amount):
            if sorted_melee_weapons:
                weapon = sorted_melee_weapons.pop()
                damage_dice = weapon.melee.melee_damage
            else:
                improvised_weapons = self._get_improvised_weapons(attacker)
                if not improvised_weapons:
                    return True

                weapon = improvised_weapons.pop()
                damage_dice = D4(1)

            success = self.make_melee_hit_roll(attacker, defender, sneak_attack=sneak_attack)
            if success:
                damage = self.make_melee_damage_roll(attacker, damage_dice, sneak_attack=sneak_attack)
                self.echo(attacker, defender, weapon, True, damage, sneak_attack=sneak_attack)
                if defender.health:
                    defender.health.take_damage(damage, attacker)
            else:
                self.echo(attacker, defender, weapon, False, 0, sneak_attack=sneak_attack)

        return True

    @staticmethod
    def _sort_melee_weapons_by_damage(attacker):
        melee_weapons = [weapon for weapon in attacker.equipment.get_wielded_items() if weapon.melee]
        melee_weapons.sort(key=lambda item: item.melee.melee_damage.sides * item.melee.melee_damage.amount)

        return melee_weapons

    @staticmethod
    def _get_improvised_weapons(attacker):
        return [weapon for weapon in attacker.equipment.get_wielded_items()]

    def echo(self, attacker, defender, weapon, success, damage, sneak_attack=False):
        # TODO I want to have a nice combat message system, I'll think about it.
        # TODO For now, this poor message.
        context = contexts.WeaponCombat(attacker, defender, weapon)
        if success:
            if sneak_attack:
                message = self.on_stealth + "for {} damage!".format(damage)
            else:
                message = self.on_success + "for {} damage!".format(damage)
        else:
            message = self.on_failure
        self.game.echo.player(message, context)
