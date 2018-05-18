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
            context = contexts.MultipleTargetAction(character, obstacles_with_size)
            if obstacles_with_size:
                message = StringBuilder(Actor, "successfully", Verb("jump", Actor), "over", Targets, "!")
            else:
                message = StringBuilder(Actor, Verb("jump", Actor), ".")

            character.location.set_local_coords(self.target_coords)
            self.game.echo.see(character, message, context)
        else:
            if obstacles_with_size:
                tripped_on = random.choice(obstacles_with_size)
                context = contexts.Action(character, tripped_on)
                message = StringBuilder(
                    Actor, Verb("collide", Actor), "with", Target, "and",
                    Verb("fall", Actor), "!"
                )
                new_pos = None
                level = character.location.level
                possible_positions = [(x, y) for x in range(-1, 1) for y in range(-1, 1)]
                while not new_pos:
                    index = random.randint(len(possible_positions) - 1)
                    try_pos = possible_positions.pop(index)
                    if try_pos == character.location.get_local_coords():
                        new_pos = try_pos
                        break
                    if not level.get_objects_by_coordinates(try_pos):
                        new_pos = try_pos
                        break
                    if not possible_positions:
                        new_pos = self.target_coords

                character.location.set_local_coords(new_pos)
                self.game.echo.see(character, message, context)
            else:
                # TODO Getting a 1 should fetch something to collide against
                # TODO If there is nothing adjacent it should just trip and fall.
                # TODO If there IS something hard to faceplant on, DAMAGE!
                random_position = self.non_blocking_tiles
                context = contexts.Action(character, None)
                message = StringBuilder(Actor, Verb("jump", Actor), ".")
                self.game.echo.see(character, message, context)
            
        return True
