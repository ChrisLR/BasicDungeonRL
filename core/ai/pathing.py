from tcod import path
from clubsandwich.geom import Point


class ComputedPath(object):
    """
    This object hooks on to the level and will invalidate itself
    whenever a tile is changed in the map.
    """
    def __init__(self, host):
        level = host.location.level
        level.register_on_tile_change_callback(self.invalidate)
        self.host = host
        self.inner_map = level.inner_map
        self.a_star = path.AStar(self.inner_map, 1.0)
        self.path = []
        self.last_destination = None

    def invalidate(self):
        self.path = []
        self.a_star = path.AStar(self.inner_map, 1.0)
        if self.last_destination:
            self.calculate(self.last_destination)

    def calculate(self, destination_coordinates):
        origin = self.host.location.get_local_coords()
        if isinstance(destination_coordinates, Point):
            destination_coordinates = (
                destination_coordinates.x,
                destination_coordinates.y)
        self.path = self.a_star.get_path(*origin, *destination_coordinates)

    def next(self):
        if self.path:
            origin = self.host.location.get_local_coords()
            next_coordinate = self.path.pop(0)
            x1, y1 = origin
            x2, y2 = next_coordinate

            return x2 - x1, y2 - y1
        else:
            self.last_destination = None
