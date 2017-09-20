class SpecialAbility(object):
    pass


class CombatBonusSpecialAbility(SpecialAbility):
    __slots__ = ["amount"]

    def __init__(self, amount):
        self.amount = amount


class DetectionSpecialAbility(SpecialAbility):
    pass


class ImmunitySpecialAbility(SpecialAbility):
    pass


class ResistanceSpecialAbility(SpecialAbility):
    pass
