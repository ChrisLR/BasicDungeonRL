from core.components.base import Component
from clubsandwich.geom import Point


class Location(Component):
    NAME = "location"
    __slots__ = ["area", "level", "_local_x", "_local_y", "region", "world_x", "world_y"]

    def __init__(self):
        super().__init__()
        self.area = None
        self.level = None
        self._local_x = 0
        self._local_y = 0
        self.region = None
        self.world_x = 0
        self.world_y = 0
        self.point = Point(self._local_x, self._local_y)

    @property
    def local_x(self):
        return self._local_x

    @property
    def local_y(self):
        return self._local_y

    def update_from_other(self, location):
        self.area = location.area
        self.level = location.level
        self.region = location.region
        self.world_x = location.world_x
        self.world_y = location.world_y
        self.set_local_coords(location.get_local_coords())

    def copy(self):
        new_instance = Location()
        new_instance.area = self.area
        new_instance.level = self.level
        new_instance._local_x = self.local_x
        new_instance._local_y = self.local_y
        new_instance.region = self.region
        new_instance.world_x = self.world_x
        new_instance.world_y = self.world_y

        return new_instance

    def get_local_coords(self):
        return self.local_x, self.local_y

    def set_local_coords(self, coordinates):
        if self.level:
            self.level.adjust_coordinates_for_object(self.host, coordinates)
        self._local_x, self._local_y = coordinates
        self.point.x = self._local_x
        self.point.y = self._local_y


class TileLocation(Location):
    def set_local_coords(self, coordinates):
        self._local_x, self._local_y = coordinates
        self.point.x = self._local_x
        self.point.y = self._local_y
