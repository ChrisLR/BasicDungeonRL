from enum import Enum


class Size(Enum):
    VerySmall = "Very Small"
    Small = "Small"
    Medium = "Medium"
    Large = "Large"
    Huge = "Huge"


feet_map = {
    Size.VerySmall: 1,
    Size.Small: 3,
    Size.Medium: 5,
    Size.Large: 10,
    Size.Huge: 20,
}


def size_in_feet(size):
    return feet_map.get(size, 0)
