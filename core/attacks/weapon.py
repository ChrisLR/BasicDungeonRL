from bflib import attacks
from core.attacks.base import MeleeAttack


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
        for _ in range(0, attack_set.amount):
            weapon = sorted_melee_weapons.pop()
            if weapon is None:
                return True

            success = cls.make_melee_hit_roll(attacker, defender)
            if success:
                damage = cls.make_melee_damage_roll(attacker, weapon.melee.damage)
                defender.health.take_damage(damage)

        return True

    @staticmethod
    def _sort_melee_weapons_by_damage(attacker):
        melee_weapons = [weapon for weapon in attacker.equipment.get_wielded_items() if weapon.melee]
        melee_weapons.sort(key=lambda item: item.melee.melee_damage.sides * item.melee.melee_damage.amount)

        return melee_weapons
