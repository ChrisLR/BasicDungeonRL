from enum import Enum


class WearLocation(Enum):
    Any = "Any"
    Arms = "arms"
    Back = "back"
    Bandolier = "bandolier"
    Belt = "belt"
    Feet = "feet"
    Face = "face"
    Hands = "hands"
    Head = "head"
    Legs = "legs"
    Neck = "neck"
    Rings = "rings"
    Torso = "torso"
    Waist = "waist"
    none = None


class WieldLocation(Enum):
    Any = "Any"
    LeftHand = "Left Hand"
    RightHand = "Right Hand"
