attacks_listing = {}
listing_by_name = {}


def register(attack_type):
    if attack_type.base_attack in attacks_listing:
        raise Exception("Attack already registered for this base_object_type.")
    elif attack_type.name in listing_by_name:
        raise Exception("Attack already registered for this name.")

    attacks_listing[attack_type.base_attack] = attack_type
    listing_by_name[attack_type.name] = attack_type

    return attack_type


def get_attack(base_attack):
    attack = attacks_listing.get(base_attack, None)
    if attack is None:
        attack_type = type(base_attack)
        if attack_type is type:
            try:
                return get_attack(base_attack.__bases__[0])
            except IndexError:
                return None
        else:
            return get_attack(attack_type)

    return attack


def get_attack_by_name(name):
    return listing_by_name.get(name)
