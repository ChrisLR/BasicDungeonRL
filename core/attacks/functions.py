import random

from core.attacks import listing


_attack_mapping = {attack.base_attack: attack for attack in listing}


def auto_attack(attacker, defender):
    possible_attacks = [attack_set for attack_set in attacker.combat.attack_sets
                        if type(attack_set.attack) in _attack_mapping
                        and _attack_mapping[type(attack_set.attack)].can_execute(attacker, defender)
                        ]

    if not possible_attacks:
        return False

    attack_set_or_chain = random.choice(possible_attacks)
    if hasattr(attack_set_or_chain, 'attack_sets'):
        attack_sets = attack_set_or_chain.attack_sets
    else:
        attack_sets = attack_set_or_chain,

    for attack_set in attack_sets:
        attack = _attack_mapping.get(type(attack_set.attack), None)
        if attack is None:
            raise Exception("Attack {} is not implemented.".format(attack_set.attack.name))
        attack.execute(attacker, defender, attack_set)

    return True
