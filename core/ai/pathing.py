from tcod import path


class ComputedPath(object):
    """
    This object hooks on to the level and will invalidate itself
    whenever a tile is changed in the map.
    """
    def __init__(self, host):
        level = self.host.location.level
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
        self.path = self.a_star.get_path(*origin, *destination_coordinates)

    def next(self):
        if self.path:
            return self.path.pop(0)
        else:
            self.last_destination = None
