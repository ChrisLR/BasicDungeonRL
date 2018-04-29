from bflib import dice
from core import contexts, events
from core.attacks import listing
from core.attacks.base import Attack
from messaging import StringBuilder, Attacker, Defender, Verb, His, AttackerWeapon, Ammunition


@listing.register
class RangedAttack(Attack):
    name = "ranged"
    base_attack = None

    def execute(self, attacker, defender, fired_weapons, distance, compatible_ammo):
        attacker.events.transmit(events.Attacking(attacker))
        for fired_weapon in fired_weapons:
            ammunition_spent = self.consume_ammunition(attacker, fired_weapon, compatible_ammo)
            context = contexts.RangedCombat(attacker, defender, fired_weapon, ammunition_spent)
            message = StringBuilder(
                Attacker, Verb("fire", Attacker), His(Attacker), AttackerWeapon, "at", Defender
            )
            if self.make_hit_roll(attacker, defender, fired_weapon, distance):
                damage = self.make_damage_roll(ammunition_spent)
                message += "hitting for %s damage!" % damage
                self.game.echo.see(attacker, message, context)
                defender.health.take_damage(damage, attacker)
            else:
                # TODO This message here could be better.
                message += "missing the shot!"
                self.game.echo.see(attacker, message, context)

        return True

    def is_proper_ammo_type(self, required_type, item):
        if item.ammunition and item.ammunition.ammunition_type == required_type:
            return True
        elif isinstance(item, required_type):
            return True
        return False

    def consume_ammunition(self, attacker, fired_weapon, compatible_ammo):
        ammunition_type = fired_weapon.ranged.ammunition_type
        for ammo_item, ammo_types in compatible_ammo.items():
            if ammunition_type in ammo_types:
                attacker.inventory.remove(ammo_item)
                return ammo_item

    def _get_attack_modifier(self, attacker, defender, fired_weapon, distance):
        modifier = 0
        if attacker.combat:
            modifier += attacker.combat.attack_bonus

        if attacker.stats:
            modifier += attacker.stats.dexterity_modifier

        # TODO If attacker is behind defender, +2 to hit roll
        # TODO If attacker invisible, +4
        # TODO If defender invisible, -4
        # TODO If defender is pinned, +4
        if not defender.health.conscious:
            modifier += 8

        range_set = fired_weapon.ranged.range_set
        if distance <= range_set.short.value:
            modifier += 1
        elif distance <= range_set.long.value:
            modifier -= 2

        return modifier

    def make_hit_roll(self, attacker, defender, fired_weapon, distance):
        target_ac = defender.combat.armor_class
        if target_ac is None:
            target_ac = 0

        modifier = self._get_attack_modifier(attacker, defender, fired_weapon, distance)
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

    def make_damage_roll(self, ammunition_spent):
        damage_dice = ammunition_spent.ammunition.ammunition_damage
        total_damage = damage_dice.roll()

        if total_damage <= 0:
            return 1
        else:
            return total_damage
