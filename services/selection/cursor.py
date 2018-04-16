from bearlibterminal import terminal
from clubsandwich.geom import Point
from clubsandwich.ui import UIScene, LabelView, RectView

from core.direction import move_direction_mapping
from services.selection.base import Selection


class CursorSelection(Selection):
    def resolve(self):
        self.view = CursorScene(self.game, self, self.executor)
        self.game.director.push_scene(self.view)


class CursorScene(UIScene):
    covers_screen = False

    def __init__(self, game, selection, executor):
        self.game = game
        self.action_mapping = game.action_mapping
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

        action = self.action_mapping.lowercase_mapping.get(val, None)
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

    def __init__(self, game, parent_scene):
        super().__init__(layout_options=game.game_scene.game_view.layout_options)
        self.parent_scene = parent_scene
        self.camera = game.camera

    def draw(self, ctx):
        cursor_position = self.parent_scene.cursor_position
        screen_position = self.camera.transform(cursor_position)
        screen_position.x += 1
        screen_position.y += 1
        ctx.print(screen_position, "X")
