from functools import partial

from clubsandwich.ui import UIScene, LabelView

from core import actionmapping
from core.actions.move import Walk
from core.direction import move_direction_mapping
from services.selection.base import Selection


class DirectionalSelection(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self, executor):
        self.view = DirectionalView(partial(self.select_targets, executor=executor))
        self.view.director.push_scene(self.view)

    @classmethod
    def select_targets(cls, direction_action, executor):
        origin = executor.location.get_local_coords()
        point_offset = move_direction_mapping.get(direction_action)
        target_coordinates = (origin[0] + point_offset[0], origin[1] + point_offset[1])
        level = executor.location.level
        targets = level.get_objects_by_coordinates(target_coordinates)

        tile = level.get_tile(target_coordinates)
        if tile:
            targets.append(tile)

        return targets


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
            self.selection.select_targets(action)
            self.director.pop_scene()
