from clubsandwich.geom import Point, Rect, Size


class Camera(object):
    def __init__(self, location, screen_size, character_focus=None):
        """
        Initialize a Camera for drawing.
        :param location: Location component
        :param screen_bounds: Size(width, height) of the boundaries of the screen on which to draw.
        """
        self.location = location
        self.screen_point_offset = Point(1, 5)
        self.screen_size = screen_size
        self.point = Point(*self.location.get_local_coords())
        self.view_rect = self.set_view_rect(self.point)
        self.character_focus = character_focus

    def transform(self, point, enforce_bounds=True):
        """
        Transforms an absolute Point(x, y) to it's relative Point(x, y)
        :param point: Absolute Point(x, y) to transform
        :param enforce_bounds: If True we will return None if it is out of bounds.
        :return: Relative Point to draw
        """
        if enforce_bounds:
            if not self.view_rect.contains(point):
                return None

        return Point(point.x - self.view_rect.x, point.y - self.view_rect.y)

    def set_view_rect(self, point):
        offset_point = Point(point.x + self.screen_point_offset.x, point.y + self.screen_point_offset.y)
        offset_size = Size(
            self.screen_size.width - self.screen_point_offset.x,
            self.screen_size.height - self.screen_point_offset.y
        )
        return Rect(offset_point, offset_size)

    def focus_on_game_object(self, game_object=None):
        if game_object is None:
            game_object = self.character_focus
            if game_object is None:
                return

        self.location.area = game_object.location.area
        self.location.level = game_object.location.level
        self.location.global_x = game_object.location.global_x
        self.location.global_y = game_object.location.global_y
        self.location.local_x = game_object.location.local_x - int(self.screen_size.width / 2)
        self.location.local_y = game_object.location.local_y - int(self.screen_size.height / 2)
        self.point = Point(*self.location.get_local_coords())
        self.view_rect = self.set_view_rect(self.point)


