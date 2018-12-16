class Combat(object):
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender


class WeaponCombat(object):
    def __init__(self, attacker, defender, attacker_weapon):
        self.attacker = attacker
        self.defender = defender
        self.attacker_weapon = attacker_weapon


class RangedCombat(object):
    def __init__(self, attacker, defender, attacker_weapon, ammunition):
        self.attacker = attacker
        self.defender = defender
        self.attacker_weapon = attacker_weapon
        self.ammunition = ammunition
