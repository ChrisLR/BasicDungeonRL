from bearlibterminal import terminal
from clubsandwich.geom import Point
from clubsandwich.ui import UIScene, LabelView, RectView

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
        views = game.game_context.game_scene.view.subviews.copy()
        self.label = LabelView("")
        self.cursor_view = CursorView(game.game_context.camera, self)
        views.append(self.label)
        views.append(self.cursor_view)
        super().__init__(views=views)
        self.executor = executor
        self.selection = selection
        self.cursor_position = Point(*executor.location.get_local_coords())

    def terminal_read(self, val):
        super().terminal_read(val)
        level = self.executor.location.level
        if val == terminal.TK_ESCAPE:
            self.selection.canceled = True
            self.director.pop_scene()

        if val == terminal.TK_ENTER:
            game_objects = level.get_objects_by_coordinates(self.cursor_position)
            self.selection.resolution = game_objects
            self.director.pop_scene()

        action = actionmapping.lowercase_mapping.get(val, None)
        if not action:
            return

        if hasattr(action, 'direction'):
            x_offset, y_offset = move_direction_mapping.get(action.direction, (0, 0))
            self.cursor_position.x += x_offset
            self.cursor_position.y += y_offset

            game_objects = level.get_objects_by_coordinates(self.cursor_position)
            if game_objects:
                self.label.text = "\n".join(
                    (game_object.name for game_object in game_objects))
            else:
                self.label.text = ""


class CursorView(RectView):
    covers_screen = False

    def __init__(self, camera, parent_scene):
        super().__init__()
        self.parent_scene = parent_scene
        self.camera = camera

    def draw(self, ctx):
        self.parent_scene.label.draw(ctx)
        origin = game.game_context.game_scene.game_view.frame.origin
        with ctx.translate(origin):
            cursor_position = self.parent_scene.cursor_position
            screen_position = self.camera.transform(cursor_position)
            screen_position.x += 1
            screen_position.y += 1
            ctx.print(screen_position, "X")

