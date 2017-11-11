from functools import partial

from clubsandwich.ui import UIScene, LabelView

from core import actionmapping
from core.actions.move import Walk
from core.direction import move_direction_mapping
from core.game.manager import game
from services.selection.base import Selection


class DirectionalSelection(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.view = DirectionalView(self)
        game.game_context.director.push_scene(self.view)

    def select_targets(self, direction):
        origin = self.executor.location.get_local_coords()
        point_offset = move_direction_mapping.get(direction)
        target_coordinates = (origin[0] + point_offset[0], origin[1] + point_offset[1])
        level = self.executor.location.level
        targets = level.get_objects_by_coordinates(target_coordinates)

        tile = level.get_tile(target_coordinates)
        if tile:
            targets.append(tile)

        self.resolution = targets


class DirectionalView(UIScene):
    covers_screen = False

    def __init__(self, selection):
        super().__init__([LabelView("Choose a direction.")])
        self.selection = selection

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if not action:
            return

        if isinstance(action, Walk) or issubclass(action, Walk):
            self.selection.select_targets(action.direction)
            self.director.pop_scene()
