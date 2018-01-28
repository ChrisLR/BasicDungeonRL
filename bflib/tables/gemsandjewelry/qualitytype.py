from enum import Enum


class QualityType(Enum):
    Junk = "Junk"
    Ornamental = "Ornamental"
    Semiprecious = "Semiprecious"
    Fancy = "Fancy"
    Precious = "Precious"
    Gem = "Gem"
    Jewel = "Jewel"


_value_map = {
    QualityType.Ornamental: 1,
    QualityType.Semiprecious: 2,
    QualityType.Fancy: 3,
    QualityType.Precious: 4,
    QualityType.Gem: 5,
    QualityType.Jewel: 6,
}
_inverse_map = {value: key for key, value in _value_map.items()}


def get_quality_value(quality_type):
    return _value_map.get(quality_type, 1)


def get_type_from_value(quality_value):
    return _inverse_map.get(quality_value, QualityType.Ornamental)
