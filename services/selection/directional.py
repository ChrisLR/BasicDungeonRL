from bearlibterminal import terminal
from clubsandwich.ui import LabelView

from core.direction import move_direction_mapping
from core.ui import CoreUIScene
from services.selection.base import Selection


class DirectionalSelection(Selection):
    def resolve(self):
        self.view = DirectionalView(self.game, self)
        self.game.director.push_scene(self.view)

    def select_targets(self, direction):
        origin = self.executor.location.get_local_coords()
        point_offset = move_direction_mapping.get(direction)
        target_coordinates = (origin[0] + point_offset[0], origin[1] + point_offset[1])
        level = self.executor.location.level
        targets = level.get_objects_by_coordinates(target_coordinates)

        tile = level.get_tile(target_coordinates)
        if tile:
            targets.add(tile)

        self.resolution = targets


class DirectionalView(CoreUIScene):
    covers_screen = False

    def __init__(self, game, selection):
        super().__init__([LabelView("Choose a direction.")])
        self.game = game
        self.selection = selection

    def terminal_read(self, val):
        super().terminal_read(val)
        if val == terminal.TK_ESCAPE:
            self.selection.canceled = True
            self.director.pop_scene()

        action = self.game.action_mapping.get_lowercase(val)
        if not action:
            return

        if hasattr(action, 'direction'):
            self.selection.select_targets(action.direction)
            self.director.pop_scene()
