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
    Up = "Up"
    Down = "Down"


move_direction_mapping = {
    Direction.NorthWest: (-1, -1),
    Direction.North: (0, -1),
    Direction.NorthEast: (1, -1),
    Direction.East: (1, 0),
    Direction.SouthEast: (1, 1),
    Direction.South: (0, 1),
    Direction.SouthWest: (-1, 1),
    Direction.West: (-1, 0),
    Direction.Up: (0, 0),
    Direction.Down: (0, 0),
}

inverse_mapping = {
    Direction.NorthWest: Direction.SouthEast,
    Direction.North: Direction.South,
    Direction.NorthEast: Direction.SouthWest,
    Direction.East: Direction.West,
    Direction.SouthEast: Direction.NorthWest,
    Direction.South: Direction.North,
    Direction.SouthWest: Direction.NorthEast,
    Direction.West: Direction.East,
    Direction.Up: Direction.Down,
    Direction.Down: Direction.Up
}


def get_inverse_direction(direction):
    return inverse_mapping.get(direction)


def get_direction_offset_by_delta(start, end):
    start_x, start_y = start
    end_x, end_y = end
    x_offset = 0
    if start_x > end_x:
        x_offset = -1
    elif start_x < end_x:
        x_offset = 1

    y_offset = 0
    if start_y > end_y:
        y_offset = -1
    elif start_y < end_y:
        y_offset = 1

    return x_offset, y_offset
