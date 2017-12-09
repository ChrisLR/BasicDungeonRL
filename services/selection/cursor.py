from bearlibterminal import terminal
from clubsandwich.ui import UIScene, LabelView

from core import actionmapping
from core.direction import move_direction_mapping
from core.game.manager import game
from services.selection.base import Selection


class CursorSelection(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.view = CursorView(self, self.executor)
        game.game_context.director.push_scene(self.view)


class CursorView(UIScene):
    covers_screen = False

    def __init__(self, selection, executor):
        super().__init__([LabelView("Choose a direction.")])
        self.executor = executor
        self.selection = selection
        self.cursor_position = executor.location.get_local_coords()

    def draw(self, ctx):
        ctx.printf(self.cursor_position, "X")

    def terminal_read(self, val):
        super().terminal_read(val)
        if val == terminal.TK_ESCAPE:
            self.selection.canceled = True
            self.director.pop_scene()

        if val == terminal.TK_ENTER:
            game_objects = self.executor.location.level.get_objects_by_coordinates(self.cursor_position)
            self.selection.resolution = game_objects
            self.director.pop_scene()

        action = actionmapping.lowercase_mapping.get(val, None)
        if not action:
            return

        if hasattr(action, 'direction'):
            self.cursor_position += move_direction_mapping.get(action.direction)
