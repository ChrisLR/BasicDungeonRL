from bflib.characters import specialabilities
from bflib.dice import D4
from core import contexts, events
from core.attacks.base import Attack
from messaging import StringBuilder, Attacker, Defender, Verb, His, AttackerWeapon


class RangedAttack(Attack):
    name = "ranged"

    def execute(self, attacker, defender, fired_weapons):
        attacker.events.transmit(events.Attacking(attacker))
        for fired_weapon in fired_weapons:
            # TODO Hit Roll, Dam Roll, apply_damage, Consume Ammo, Echo
            pass

        return True

