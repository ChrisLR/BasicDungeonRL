from core.actions.base import Action
from core.actions.bump import Bump
from core.direction import Direction, move_direction_mapping


class Walk(Action):
    direction = None

    @classmethod
    def from_direction(cls, direction):
        return _walk_direction_mapping.get(direction)

    @classmethod
    def can_execute(cls, character, selection=None):
        # TODO Some characters might not be in a condition to move.
        return True

    @classmethod
    def execute(cls, character, selection=None):
        if cls.direction:
            direction = cls.direction
        else:
            return False

        delta_x, delta_y = move_direction_mapping.get(direction)
        x = character.location.local_x
        y = character.location.local_y
        current_level = character.location.level
        new_x = x + delta_x
        new_y = y + delta_y
        if new_x < 0 or new_x >= current_level.max_x:
            return
        if new_y < 0 or new_y >= current_level.max_y:
            return

        new_coords = (new_x, new_y)
        tile = current_level.get_tile(new_coords)
        if tile is None:
            return False

        if tile.openable and tile.openable.closed:
            tile.openable.open()
            return False

        if tile.blocking:
            return False

        game_objects = current_level.get_objects_by_coordinates(new_coords)
        if game_objects:
            for game_object in game_objects:
                if game_object.blocking:
                    return Bump.execute(character, game_object)

        character.location.set_local_coords(new_coords)
        return True


class WalkNW(Walk):
    direction = Direction.NorthWest


class WalkN(Walk):
    direction = Direction.North


class WalkNE(Walk):
    direction = Direction.NorthEast


class WalkE(Walk):
    direction = Direction.East


class WalkSE(Walk):
    direction = Direction.SouthEast


class WalkS(Walk):
    direction = Direction.South


class WalkSW(Walk):
    direction = Direction.SouthWest


class WalkW(Walk):
    direction = Direction.West


_walk_direction_mapping = {
    Direction.North: WalkN,
    Direction.NorthEast: WalkNE,
    Direction.East: WalkE,
    Direction.SouthEast: WalkSE,
    Direction.South: WalkS,
    Direction.SouthWest: WalkSW,
    Direction.West: WalkW,
    Direction.NorthWest: WalkNW
}