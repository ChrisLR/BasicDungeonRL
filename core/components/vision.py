import tdl

from core.components import Component
from core.util.distance import manhattan_distance_to


class Vision(Component):
    NAME = 'vision'
    __slots__ = ["fov", "fov_range"]

    def __init__(self, fov_range=3):
        super().__init__()
        self.fov = None
        self.fov_range = fov_range

    def can_see_object(self, game_object):
        if game_object.location.get_local_coords() in self.fov:
            return self._can_see(game_object)

    def _can_see(self, game_object):
        return can_see(self.host, game_object)

    def round_update(self):
        self.update_field_of_vision()

    def copy(self):
        return Vision()

    def update_field_of_vision(self):
        x, y = self.host.location.get_local_coords()
        self.fov = tdl.map.quick_fov(x, y, self.is_transparent, 'basic', radius=self.fov_range)

    def is_transparent(self, x, y):
        if x <= 0 or y <= 0:
            return False

        tile = self.host.location.level.get_tile((x, y))
        if tile and tile.opaque:
            return False
        return True


class SimpleVision(Component):
    NAME = 'vision'
    __slots__ = ["fov", "fov_range"]

    def __init__(self, fov_range=3):
        """
        This SimpleVision only keeps track of GameObjects
        :param fov_range: Range of Vision
        """
        super().__init__()
        self.seen_objects = None
        self.fov_range = fov_range

    def can_see_object(self, game_object):
        if self.seen_objects is None:
            self.update_vision()
        return game_object in self.seen_objects

    def round_update(self):
        self.update_vision()

    def copy(self):
        return Vision()

    def update_vision(self):
        coordinate = self.host.location.get_local_coords()
        level_objects = self.host.location.level.game_objects
        in_range_objects = [
            game_object for game_object in level_objects
            if game_object is not self.host and manhattan_distance_to(
                coordinate,
                game_object.location.get_local_coords()
            ) <= self.fov_range
        ]
        visible_objects = {
            game_object for game_object in in_range_objects
            if self._can_see(game_object) and self.raycast(
                coordinate, game_object.location.get_local_coords()
            )
        }
        self.seen_objects = visible_objects

    def raycast(self, origin, destination):
        level = self.host.location.level
        current_x, current_y = origin
        destination_x, destination_y = destination
        while (current_x, current_y) != destination:
            tile = level.get_tile((current_x, current_y))
            if tile and tile.opaque:
                return False

            if current_x < destination_x:
                current_x += 1
            elif current_x > destination_x:
                current_x -= 1

            if current_y < destination_y:
                current_y += 1
            elif current_y > destination_y:
                current_y -= 1

        return True

    def _can_see(self, game_object):
        return can_see(self.host, game_object)


def can_see(host, game_object):
    if host.health and (not host.health.conscious or host.health.dead):
        return False

    visible = game_object.query.visibility()
    if visible is True:
        return True

    # TODO Here, we could iterate through what conditions would allow a host
    # TODO to counter specific anti visibilities.
    return False
