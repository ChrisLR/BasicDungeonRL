from bflib import dice


class MeleeAttack(object):
    base_attack = None
    needs_weapon = False

    @classmethod
    def make_melee_hit_roll(cls, attacker, defender):
        target_ac = defender.combat.armor_class
        modifier = 0
        modifier += attacker.combat.attack_bonus
        modifier += attacker.stats.strength_modifier if attacker.stats else 0
        # TODO If attacker is behind defender, +2 to hit roll
        # TODO If attacker invisible, +4
        # TODO If defender invisible, -4
        # TODO If defender is pinned, +4
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
    def make_melee_damage_roll(cls, attacker, damage_dice, other_modifier=0):
        total_damage = 0
        total_damage += damage_dice.roll()
        total_damage += attacker.stats.strength_modifier if attacker.stats else 0
        total_damage += other_modifier
        if total_damage <= 0:
            return 1
        else:
            return total_damage
