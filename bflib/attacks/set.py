class AttackSet(object):
    __slots__ = ["amount", "attack", "special_properties"]

    def __init__(self, attack, amount=1, special_properties=None):
        self.amount = amount  # type: int
        self.attack = attack  # type :
        self.special_properties = special_properties


class AttackChain(object):
    __slots__ = ["attack_sets"]

    def __init__(self, *attack_sets):
        self.attack_sets = list(attack_sets)