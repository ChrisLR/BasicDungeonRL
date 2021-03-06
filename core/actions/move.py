from core import events
from core.actions.base import Action
from core.direction import Direction, move_direction_mapping


class Walk(Action):
    direction = None

    @classmethod
    def from_direction(cls, direction):
        return _walk_direction_mapping.get(direction)

    def can_execute(self, character, target_selection=None):
        # TODO Some characters might not be in a condition to move.
        return True

    def execute(self, character, target_selection=None):
        if self.direction:
            direction = self.direction
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

        if tile.blocking:
            return False

        game_objects = current_level.get_objects_by_coordinates(new_coords)
        if game_objects:
            for game_object in game_objects:
                if game_object.blocking:
                    bump = self.game.actions.get_action_by_name("bump")
                    return bump.execute(character, (game_object,))

        character.location.set_local_coords(new_coords)

        character.events.transmit(events.Moved(character))
        if tile:
            tile.events.transmit(events.WalkedOn(character))

        if game_objects:
            for game_object in game_objects:
                game_object.events.transmit(events.WalkedOn(character))

        return True


class WalkNW(Walk):
    name = "walk_nw"
    direction = Direction.NorthWest


class WalkN(Walk):
    name = "walk_n"
    direction = Direction.North


class WalkNE(Walk):
    name = "walk_ne"
    direction = Direction.NorthEast


class WalkE(Walk):
    name = "walk_e"
    direction = Direction.East


class WalkSE(Walk):
    name = "walk_se"
    direction = Direction.SouthEast


class WalkS(Walk):
    name = "walk_s"
    direction = Direction.South


class WalkSW(Walk):
    name = "walk_sw"
    direction = Direction.SouthWest


class WalkW(Walk):
    name = "walk_w"
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
