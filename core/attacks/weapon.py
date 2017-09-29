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
        weapons = (
            weapon for weapon in sorted(
                attacker.equipment.get_wielded_items(),
                key=lambda item: item.melee.damage.sides * item.melee.damage.amount)
        )
        for _ in range(0, attack_set):
            weapon = next(weapons, None)
            if weapon is None:
                return True

            success = cls.make_melee_hit_roll(attacker, defender)
            if success:
                damage = cls.make_melee_damage_roll(attacker, weapon.melee.damage)
                defender.health.take_damage(damage)

        return True
