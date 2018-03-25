from clubsandwich.geom import Point, Size
from clubsandwich.ui import RectView

from ui.camera import Camera


class GameView(RectView):
    def __init__(self, game, **kwargs):
        super().__init__(fill=True,  **kwargs)
        self.game = game
        player = self.game.player
        self.camera = Camera(location=player.location.copy(), screen_size=Size(120, 30))
        self.camera.character_focus = player
        self.game.camera = self.camera

    def draw(self, ctx):
        player = self.game.player
        self.camera.focus_on_game_object()

        if player.vision.fov:
            self.draw_tiles(player.vision.fov, ctx)
            self.draw_displays(player.vision.fov, ctx)

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

    def draw_displays(self, viewer_fov, ctx):
        current_level = self.camera.location.level
        for priority in sorted(current_level.displays.keys(), key=lambda k: k.value):
            for game_object in current_level.displays[priority]:
                x, y = game_object.location.get_local_coords()
                if (x, y) in viewer_fov:
                    relative_point = self.camera.transform(Point(x, y))
                    if relative_point is not None:
                        ctx.printf(
                            relative_point,
                            game_object.display.get_draw_info()
                        )
