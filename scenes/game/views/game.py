import tdl
from clubsandwich.geom import Point, Size
from clubsandwich.ui import RectView

from ui.camera import Camera


class GameView(RectView):
    def __init__(self, game_context, **kwargs):
        super().__init__(fill=True, **kwargs)
        self.game_context = game_context
        player = self.game_context.player
        self.camera = Camera(location=player.location.copy(), screen_size=Size(120, 30))
        self.camera.character_focus = player

    def draw(self, ctx):
        player = self.game_context.player
        current_level = player.location.level
        self.camera.focus_on_game_object()
        self.set_tiles_background_color(ctx)

        player_x = player.location.local_x
        player_y = player.location.local_y

        def is_transparent_callback(x, y):
            if x <= 0 or y <= 0:
                return False
            return self.is_transparent(current_level, x, y)

        player.fov = tdl.map.quickFOV(player_x, player_y, is_transparent_callback, 'basic')

        self.draw_tiles(player.fov, ctx)
        self.draw_displays(player.fov, ctx)

    def draw_tiles(self, viewer_fov, ctx):
        current_level = self.camera.location.level
        for x, y in viewer_fov:
            tile = current_level.get_tile((x, y))
            if not tile:
                continue

            relative_point = self.camera.transform(Point(x, y))
            if relative_point is None:
                continue

            ctx.printf(relative_point, tile.display.get_draw_info())
            tile.is_explored = True

    def draw_displays(self, viewer_fov, ctx):
        current_level = self.camera.location.level
        for priority in sorted(current_level.displays.keys()):
            for game_object in current_level.displays[priority]:
                x, y = game_object.location.get_local_coords()
                if (x, y) in viewer_fov:
                    relative_point = self.camera.transform(Point(x, y))
                    if relative_point is not None:
                        ctx.printf(
                            relative_point,
                            game_object.display.get_draw_info()
                        )

    def set_tiles_background_color(self, ctx):
        current_level = self.camera.location.level
        for y in range(current_level.height):
            for x in range(current_level.width):
                relative_point = self.camera.transform(Point(x, y))
                if relative_point is not None:
                    tile = current_level.maze[x][y]
                    wall = tile.block_sight
                    ground = tile.is_ground

                    if tile.is_explored:
                        if wall:
                            ctx.printf(relative_point, '[color=gray]#')
                        elif ground:
                            ctx.printf(relative_point, '[color=gray].')

    @staticmethod
    def is_transparent(level, x, y):
        tile = level.get_tiles((x, y))
        if tile and tile.opaque:
            return False
        return True
