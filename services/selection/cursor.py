from bearlibterminal import terminal
from clubsandwich.ui import UIScene, LabelView, RectView
from clubsandwich.geom import Point

from core import actionmapping
from core.direction import move_direction_mapping
from core.game.manager import game
from services.selection.base import Selection


class CursorSelection(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.view = CursorScene(self, self.executor)
        game.game_context.director.push_scene(self.view)


class CursorScene(UIScene):
    covers_screen = False

    def __init__(self, selection, executor):
        self.label = LabelView("")
        self.cursor_view = CursorView(game.game_context.camera, self)
        super().__init__([self.label, self.cursor_view])
        self.executor = executor
        self.selection = selection
        self.cursor_position = Point(*executor.location.get_local_coords())

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
            x_offset, y_offset = move_direction_mapping.get(action.direction, (0, 0))
            self.cursor_position.x += x_offset
            self.cursor_position.y += y_offset

            


class CursorView(RectView):
    covers_screen = False

    def __init__(self, camera, parent_scene):
        super().__init__(clear=True)
        self.parent_scene = parent_scene
        self.camera = camera

    def draw(self, ctx):
        super().draw(ctx)
        game_scene = next((
            scene for scene in self.parent_scene.director.scene_stack
            if hasattr(scene, 'game_view')))
        game_scene.game_view.draw(ctx)
        cursor_position = self.parent_scene.cursor_position
        screen_position = self.camera.transform(cursor_position, enforce_bounds=False)
        ctx.printf(screen_position, "X")

