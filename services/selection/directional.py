from functools import partial

from clubsandwich.ui import UIScene, LabelView

from core import actionmapping
from core.actions.move import Walk
from core.direction import move_direction_mapping
from services.selection.base import Selection


class DirectionalSelection(Selection):
    @classmethod
    def select(cls, requester, target_type):
        return DirectionalView(partial(cls.select_targets, requester=requester, target_type=target_type))

    @classmethod
    def select_targets(cls, direction, requester, target_type):
        origin = requester.location.get_local_coords()
        point_offset = move_direction_mapping.get(direction)
        target_coordinates = origin + point_offset
        level = requester.location.level
        possible_targets = level.get_objects_by_coordinates(target_coordinates)

        final_targets = []
        for target in possible_targets:
            if not target_type or isinstance(target, target_type) or issubclass(target, target_type):
                final_targets.append(target)

        tile = level.get_tile(target_coordinates)
        if not target_type or isinstance(tile, target_type) or issubclass(tile, target_type):
            final_targets.append(tile)

        return cls(final_targets)


class DirectionalView(UIScene):
    covers_screen = False

    def __init__(self, selection_callback):
        super().__init__([LabelView("Choose a direction.")])
        self.selection_callback = selection_callback

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if not action:
            return

        if isinstance(action, Walk) or issubclass(action, Walk):
            self.director.pop_scene()
            self.selection_callback(action.direction)
