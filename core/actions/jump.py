from core.actions.base import Action
from services.selection import CursorSelection, filters
from services.selection.base import TargetSelectionSet
from core.tiles.base import Tile
from core.util import distance
from bflib import skills, sizes
from messaging import StringBuilder, Actor, Verb, Targets, Target
from core import contexts
import random


class Jump(Action):
    name = "jump"
    target_selection = TargetSelectionSet(
        selections=CursorSelection
    )
    # TODO Cursor should use a maximum distance

    def __init__(self, game):
        super().__init__(game)
        self.obstacles = None
        self.distance = None
        self.target_coords = None
        self.non_blocking_tiles = None

    def can_execute(self, character, target_selection=None):
        if not target_selection:
            return False

        if not character.skills:
            return False

        start_location = character.location
        target_location = target_selection[0].location
        if not start_location or not target_location:
            return False

        start_coords = start_location.get_local_coords()
        target_coords = target_location.get_local_coords()

        self.distance = distance.manhattan_distance_to(start_coords, target_coords)
        obstacles = start_location.level.get_objects_by_line(start_coords, target_coords)

        blocking_tiles = [tile for tile in obstacles
                          if isinstance(tile, Tile) and tile.blocking]
        blocking_tile = next(blocking_tiles, None)
        if blocking_tile:
            self.game.echo.player(
                character,
                message="You cannot jump through %s !" % blocking_tile.name
            )
            return False

        self.non_blocking_tiles = obstacles
        self.obstacles = [obs for obs in obstacles if not isinstance(obs, Tile)]
        self.target_coords = target_coords

        return True

    def execute(self, character, target_selection=None):
        obstacles_with_size = [obstacle for obstacle in self.obstacles if obstacle.size]
        obstacle_penalties = sum(
            [sizes.size_in_feet(obstacle.size.score)
             for obstacle in obstacles_with_size]
        )
        required_roll = self.distance + obstacle_penalties
        roll_result = character.skills.roll_check(skills.Jump)

        if roll_result >= required_roll:
            self._jump_successfully(character, obstacles_with_size)
        elif roll_result == 1:
            self._critical_failure_jump(character)
        else:
            self._fail_jump(character)
            
        return True

    def _jump_successfully(self, character, obstacles_with_size):
        context = contexts.MultipleTargetAction(character, obstacles_with_size)
        if obstacles_with_size:
            message = StringBuilder(Actor, "successfully", Verb("jump", Actor), "over",
                                    Targets, "!")
        else:
            message = StringBuilder(Actor, Verb("jump", Actor), ".")

        self.game.echo.see(character, message, context)
        character.location.set_local_coords(self.target_coords)

    def _fail_jump(self, character):
        new_pos = self._select_random_tile_with_offset(character, True)
        context = contexts.Action(character, None)
        message = StringBuilder(Actor, Verb("trip", Actor), "while trying to jump!")
        self.game.echo.see(character, message, context)
        character.location.set_local_coords(new_pos)

    def _critical_failure_jump(self, character):
        new_pos = self._select_random_tile_with_offset(character, False)
        context = contexts.Action(character, None)
        message = StringBuilder(Actor, Verb("trip", Actor), "and",
                                Verb("faceplant", Actor), "into")
        # TODO Faceplant on the ground, or into something blocking.
        # TODO IF blocking, double damage
        self.game.echo.see(character, message, context)
        character.location.set_local_coords(new_pos)

    def _select_random_tile_with_offset(self, character, safe=False):
        level = character.location.level
        start_x, start_y = character.location.get_local_coords()
        end_x, end_y = self.target_coords
        offset_x, offset_y = random.randint(-1, 1), random.randint(-1, 1)
        possible_positions = [(x + offset_x, y + offset_y)
                              for x in range(start_x, end_x)
                              for y in range(start_y, end_y)]
        new_pos = None
        while not new_pos:
            index = random.randint(len(possible_positions) - 1)
            try_pos = possible_positions.pop(index)

            if try_pos == character.location.get_local_coords():
                return try_pos
            if safe:
                obstacles = level.get_objects_by_coordinates(try_pos)
                tile = level.get_tile(try_pos)
                if not obstacles and not (tile and tile.blocking):
                    return True
            if not possible_positions:
                return self.target_coords
