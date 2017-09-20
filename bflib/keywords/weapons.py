from enum import Enum


class WeaponWieldKeyword(Enum):
    CanWield = 0
    CannotWield = 1
    NeedsTwoHands = 2
