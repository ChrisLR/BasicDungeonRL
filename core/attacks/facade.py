import random

from core.attacks import listing


class Facade(object):
    def __init__(self, game):
        self.game = game

    def get_attack_by_name(self, name):
        attack_type = listing.get_attack_by_name(name)
        if attack_type is not None:
            return attack_type(self.game)
        return None

    def get_possible_attacks(self, attacker, defender):
        possible_attacks = []
        for attack_set in attacker.combat.attack_sets:
            attack = listing.get_attack(attack_set.attack)
            if attack is not None:
                attack = attack(self.game)
                if attack.can_execute(attacker, defender):
                    possible_attacks.append(attack_set)

        return possible_attacks

    def auto_attack(self, attacker, defender):
        possible_attacks = self.get_possible_attacks(attacker, defender)
        if not possible_attacks:
            return False

        attack_set_or_chain = random.choice(possible_attacks)
        if hasattr(attack_set_or_chain, 'attack_sets'):
            attack_sets = attack_set_or_chain.attack_sets
        else:
            attack_sets = attack_set_or_chain,

        for attack_set in attack_sets:
            attack = listing.get_attack(attack_set.attack)
            if attack is None:
                raise Exception("Attack {} is not implemented.".format(attack_set.attack.name))
            attack = attack(self.game)
            attack.execute(attacker, defender, attack_set)

        return True
