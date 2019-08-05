from tcod import path
from clubsandwich.geom import Point
from core.direction import move_direction_mapping
from core.util import manhattan_distance_to


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
        self.a_star = path.AStar(self.inner_map, 0.0)
        self.path = []
        self.last_destination = None

    def invalidate(self):
        self.path = []
        self.a_star = path.AStar(self.inner_map, 0.0)
        if self.last_destination:
            self.calculate(self.last_destination)

    def calculate(self, destination_coordinates):
        self.last_destination = destination_coordinates
        origin = self.host.location.get_local_coords()
        if isinstance(destination_coordinates, Point):
            destination_coordinates = (
                destination_coordinates.x,
                destination_coordinates.y)
        self.path = self.a_star.get_path(*origin, *destination_coordinates)
        if not self.path:
            self.path = self.find_close_walkable_point(origin, destination_coordinates)

    def find_close_walkable_point(self, origin, target, recursion=0, sought_coords=None):
        if sought_coords is None:
            sought_coords = set()

        if recursion > 9:
            return

        level = self.host.location.level
        x1, y1 = target
        neighbors = [
            (x1 + x2, y1 + y2)
            for x2, y2 in move_direction_mapping.values()
        ]

        if all(neighbor in sought_coords for neighbor in neighbors):
            return

        walkable_neighbors = [
            coord for coord in neighbors
            if coord not in sought_coords
            and level.is_coordinate_in_bounds(coord)
            and self.inner_map.walkable[coord]
        ]

        if not walkable_neighbors:
            return

        walkable_neighbors.sort(key=lambda coord: manhattan_distance_to(origin, coord))

        path = None
        for neighbor in walkable_neighbors:
            path = self.a_star.get_path(*origin, *neighbor)
            if path:
                self.last_destination = neighbor
                break

        if path:
            return path

        sought_coords.update(neighbors)
        return self.find_close_walkable_point(
            origin, walkable_neighbors[0], recursion + 1, sought_coords)

    def next(self):
        if self.path:
            origin = self.host.location.get_local_coords()
            next_coordinate = self.path.pop(0)
            x1, y1 = origin
            x2, y2 = next_coordinate

            return x2 - x1, y2 - y1
        else:
            self.last_destination = None
