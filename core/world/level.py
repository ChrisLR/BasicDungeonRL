from core.gameobject import GameObject
from clubsandwich.geom import Point
from tcod import map as tcod_map


class Level(GameObject):
    __slots__ = [
        "displays", "inner_map", "tiles", "max_x", "max_y",
        "objects_by_coords", "on_tile_change_callbacks",
        "_game_objects"
    ]

    def __init__(self, max_x, max_y):
        super().__init__()
        self.displays = {}
        self.tiles = {}
        self.max_x = max_x
        self.max_y = max_y
        self.objects_by_coords = {}
        self._game_objects = []
        self.inner_map = tcod_map.Map(max_x, max_y)
        self.on_tile_change_callbacks = []

    def register_on_tile_change_callback(self, callback):
        if callback not in self.on_tile_change_callbacks:
            self.on_tile_change_callbacks.append(callback)

    @property
    def game_objects(self):
        return self._game_objects

    def add_object(self, game_object):
        display = game_object.display
        if display:
            display_list = self.displays.get(display.priority, None)
            if display_list is None:
                display_list = []
                self.displays[display.priority] = display_list

            display_list.append(game_object)

        location = game_object.location
        if location:
            location.level = self
            coords = location.get_local_coords()
            object_set = self.objects_by_coords.get(coords)
            if not object_set:
                object_set = set()
                self.objects_by_coords[coords] = object_set
            object_set.add(game_object)

        self._game_objects.append(game_object)

    def remove_object(self, game_object):
        display = game_object.display
        if display:
            self.displays[display.priority].remove(game_object)

        location = game_object.location
        if location:
            coords = location.get_local_coords()
            object_set = self.objects_by_coords.get(coords)
            if object_set:
                object_set.remove(game_object)

        self._game_objects.remove(game_object)

    def add_tile(self, coordinates, tile_class):
        x, y = coordinates
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        tile_instance = tile_class()
        self.tiles[coordinates] = tile_instance
        self.inner_map.walkable[coordinates] = not tile_instance.blocking
        self.inner_map.transparent[coordinates] = not tile_instance.opaque
        self.call_on_tile_change()

    def get_tile(self, coordinates):
        tile = self.tiles.get(coordinates, None)
        return tile

    def remove_tile(self, coordinates):
        del self.tiles[coordinates]
        self.inner_map.walkable[coordinates] = False
        self.inner_map.transparent[coordinates] = False
        self.call_on_tile_change()

    def get_objects_by_coordinates(self, coordinates):
        if isinstance(coordinates, Point):
            return self.objects_by_coords.get((coordinates.x, coordinates.y), set())
        return self.objects_by_coords.get(coordinates, set())

    def adjust_coordinates_for_object(self, game_object, new_coordinates):
        old_coordinates = game_object.location.get_local_coords()
        old_object_set = self.objects_by_coords.get(old_coordinates)
        if old_object_set and game_object in old_object_set:
            old_object_set.remove(game_object)

        object_set = self.objects_by_coords.get(new_coordinates)
        if not object_set:
            object_set = set()
            self.objects_by_coords[new_coordinates] = object_set
        object_set.add(game_object)

    def call_on_tile_change(self):
        for callback in self.on_tile_change_callbacks:
            callback()
