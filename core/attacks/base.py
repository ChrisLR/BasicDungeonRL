from bflib import dice
import inspect


class MeleeAttack(object):
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


class RangedAttack(object):
    def __init__(self, base_attack, attacker, defender):
        self.base_attack = base_attack
        self.attacker = attacker
        self.defender = defender
        self.success = None
        self.total_damage = 0

    def execute(self):
        self.success = self.make_hit_roll()
        if self.success:
            self.total_damage = self.make_damage_roll()

    def _get_attack_modifier(self):
        modifier = 0
        if self.attacker.combat:
            modifier += self.attacker.combat.attack_bonus

        if self.attacker.stats:
            modifier += self.attacker.stats.dexterity_modifier
        # TODO If attacker is behind defender, +2 to hit roll
        # TODO If attacker invisible, +4
        # TODO If defender invisible, -4
        # TODO If defender is pinned, +4
        if not self.defender.health.conscious:
            modifier += 8

        return modifier

    def _get_defender_ac(self):
        return self.defender.combat.armor_class

    def make_hit_roll(self):
        target_ac = self._get_defender_ac()
        if target_ac is None:
            target_ac = 0

        modifier = self._get_attack_modifier()
        modifier += self.base_attack.attack_bonus
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

    def make_damage_roll(self):
        damage_dice = self.base_attack.damage_dice
        total_damage = 0
        if inspect.isclass(damage_dice):
            total_damage += damage_dice.manual_roll(1)
        else:
            total_damage += damage_dice.roll()

        if total_damage <= 0:
            return 1
        else:
            return total_damage
