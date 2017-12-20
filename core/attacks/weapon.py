from bflib import attacks
from bflib.dice import D4
from core.attacks import listing
from core.attacks.base import MeleeAttack
from services.echo import functions as echo_functions
from services.echo.service import echo_service


@listing.register
class WeaponAttack(MeleeAttack):
    base_attack = attacks.WeaponAttack

    @classmethod
    def can_execute(cls, attacker, defender):
        if attacker.equipment.wielded_items:
            return True
        return False

    @classmethod
    def execute(cls, attacker, defender, attack_set):
        sorted_melee_weapons = cls._sort_melee_weapons_by_damage(attacker)

        for _ in range(1, attack_set.amount):
            if sorted_melee_weapons:
                weapon = sorted_melee_weapons.pop()
                damage_dice = weapon.melee.melee_damage
            else:
                improvised_weapons = cls._get_improvised_weapons(attacker)
                if not improvised_weapons:
                    return True

                weapon = improvised_weapons.pop()
                damage_dice = D4(1)

            success = cls.make_melee_hit_roll(attacker, defender)
            if success:
                damage = cls.make_melee_damage_roll(attacker, damage_dice)
                echo_message_success(attacker, defender, weapon, damage)
                if defender.health:
                    defender.health.take_damage(damage)
            else:
                echo_message_failure(attacker, defender)

        return True

    @staticmethod
    def _sort_melee_weapons_by_damage(attacker):
        melee_weapons = [weapon for weapon in attacker.equipment.get_wielded_items() if weapon.melee]
        melee_weapons.sort(key=lambda item: item.melee.melee_damage.sides * item.melee.melee_damage.amount)

        return melee_weapons

    @staticmethod
    def _get_improvised_weapons(attacker):
        return [weapon for weapon in attacker.equipment.get_wielded_items()]


def echo_message_success(attacker, defender, weapon, damage):
    # TODO I want to have a nice combat message system, I'll think about it.
    # TODO For now, this poor message.
    if echo_functions.is_player(attacker):
        message = "You hit {} with your {} for {} damage!"
        message = message.format(echo_functions.name_or_you(defender), weapon.name, damage)
    else:
        message = "{} hits {} with {} for {} damage!"
        message = message.format(
            echo_functions.name_or_you(attacker),
            echo_functions.name_or_you(defender),
            weapon.name,
            damage
        )
    echo_service.echo(message)


def echo_message_failure(attacker, defender):
    # TODO This poor message here too :(
    if echo_functions.is_player(attacker):
        message = "You miss {} !"
        message = message.format(echo_functions.name_or_you(defender))
    else:
        message = "{} misses {} !"
        message = message.format(echo_functions.name_or_you(attacker),
                                 echo_functions.name_or_you(defender))
    echo_service.echo(message)
