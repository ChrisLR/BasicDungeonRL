from enum import Enum


class WearLocation(Enum):
    Any = "Any"
    Back = "back"
    Bandolier = "bandolier"
    Belt = "belt"
    Feet = "feet"
    Torso = "torso"
    Arms = "Arms"
    Legs = "Legs"
    Waist = "waist"
    none = None


class WieldLocation(Enum):
    Any = "Any"
    LeftHand = "Left Hand"
    RightHand = "Right Hand"
