from enum import Enum


class Direction(Enum):
    North = "North"
    NorthEast = "North East"
    East = "East"
    SouthEast = "South East"
    South = "South"
    SouthWest = "South West"
    West = "West"
    NorthWest = "North West"


move_direction_mapping = {
    Direction.NorthWest: (-1, -1),
    Direction.North: (0, -1),
    Direction.NorthEast: (1, -1),
    Direction.East: (1, 0),
    Direction.SouthEast: (1, 1),
    Direction.South: (0, 1),
    Direction.SouthWest: (-1, 1),
    Direction.West: (-1, 0),
}
