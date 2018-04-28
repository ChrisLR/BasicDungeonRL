from bflib import dice
import inspect


class Attack(object):
    def __init__(self, game):
        self.game = game


class MeleeAttack(Attack):
    base_attack = None
    needs_weapon = False

    @classmethod
    def make_melee_hit_roll(cls, attacker, defender, sneak_attack=False):
        target_ac = defender.combat.armor_class
        if target_ac is None:
            target_ac = 0
        modifier = 0
        modifier += attacker.combat.attack_bonus
        modifier += attacker.stats.strength_modifier if attacker.stats else 0
        # TODO If attacker is behind defender, +2 to hit roll
        # TODO If attacker invisible, +4
        # TODO If defender invisible, -4
        # TODO If defender is pinned, +
        if sneak_attack:
            modifier += 4

        if not defender.health.conscious:
            modifier += 8

        roll = dice.D20.manual_roll(1)
        if roll == 1:
            return False

        if roll == 20:
            # TODO Some defenders CANNOT be hit, it should still fail.
            return True

        roll += modifier
        if roll >= target_ac:
            # TODO Some defenders CANNOT be hit, it should still fail.
            return True
        else:
            return False

    @classmethod
    def make_melee_damage_roll(cls, attacker, damage_dice, other_modifier=0, sneak_attack=False):

        total_damage = 0
        if inspect.isclass(damage_dice):
            total_damage += damage_dice.manual_roll(1)
        else:
            total_damage += damage_dice.roll()
        total_damage += attacker.stats.strength_modifier if attacker.stats else 0
        total_damage += other_modifier
        if total_damage <= 0:
            if sneak_attack:
                return 2
            else:
                return 1
        else:
            if sneak_attack:
                return total_damage * 2
            else:
                return total_damage
