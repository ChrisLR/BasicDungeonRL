import random

from core.attacks import listing


_attack_mapping = {attack.base_attack: attack for attack in listing}


def get_possible_attacks(attacker, defender):
    possible_attacks = []
    for attack_set in attacker.combat.attack_sets:
        if attack_set.attack in _attack_mapping:
            if _attack_mapping[attack_set.attack].can_execute(attacker, defender):
                possible_attacks.append(attack_set)

    return possible_attacks


def auto_attack(attacker, defender):
    possible_attacks = get_possible_attacks(attacker, defender)
    if not possible_attacks:
        return False

    attack_set_or_chain = random.choice(possible_attacks)
    if hasattr(attack_set_or_chain, 'attack_sets'):
        attack_sets = attack_set_or_chain.attack_sets
    else:
        attack_sets = attack_set_or_chain,

    for attack_set in attack_sets:
        attack = _attack_mapping.get(attack_set.attack, None)
        if attack is None:
            raise Exception("Attack {} is not implemented.".format(attack_set.attack.name))
        attack.execute(attacker, defender, attack_set)

    return True
