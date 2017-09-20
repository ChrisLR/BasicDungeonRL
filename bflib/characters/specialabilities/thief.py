from bflib.characters.specialabilities.base import SpecialAbility


class ThiefAbility(SpecialAbility):
    def __init__(self, value):
        self.value = value


class ClimbWalls(ThiefAbility):
    pass


class Hide(ThiefAbility):
    pass


class Listen(ThiefAbility):
    pass


class MoveSilently(ThiefAbility):
    pass


class OpenLock(ThiefAbility):
    pass


class PickPockets(ThiefAbility):
    pass


class RemoveTraps(ThiefAbility):
    pass


class SneakAttack(ThiefAbility):
    pass
