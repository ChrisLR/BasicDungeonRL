from core.gameobject import GameObject
from clubsandwich.geom import Point
from tcod import map as tcod_map
import inspect


class Level(GameObject):
    __slots__ = [
        "displays", "inner_map", "tiles", "max_x", "max_y",
        "objects_by_coords", "on_tile_change_callbacks",
        "_game_objects", "rooms", "room_grid"
    ]

    def __init__(self, max_x, max_y):
        super().__init__()
        self.displays = {}
        self.tiles = {}
        self.max_x = max_x
        self.max_y = max_y
        self.objects_by_coords = {}
        self._game_objects = set()
        self.inner_map = tcod_map.Map(max_x, max_y)
        self.on_tile_change_callbacks = []
        self.room_grid = {}
        self.rooms = []

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
            self.reset_walkable_for_coordinate(coords, object_set)

        self._game_objects.add(game_object)

    def remove_object(self, game_object):
        display = game_object.display
        if display:
            try:
                self.displays[display.priority].remove(game_object)
            except ValueError:
                pass

        location = game_object.location
        if location:
            coords = location.get_local_coords()
            object_set = self.objects_by_coords.get(coords)
            if object_set:
                try:
                    object_set.remove(game_object)
                except ValueError:
                    pass
            self.reset_walkable_for_coordinate(coords, object_set)

        self._game_objects.discard(game_object)

    def add_tile(self, coordinates, tile):
        x, y = coordinates
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        if inspect.isclass(tile):
            tile = tile()

        self.tiles[coordinates] = tile
        self.set_inner_walkable(coordinates, not tile.blocking)
        self.set_inner_transparent(coordinates, not tile.opaque)
        self.call_on_tile_change()

    def get_tile(self, coordinates):
        tile = self.tiles.get(coordinates, None)
        return tile

    def remove_tile(self, coordinates):
        del self.tiles[coordinates]
        self.set_inner_walkable(coordinates, False)
        self.set_inner_transparent(coordinates, False)
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

        self.reset_walkable_for_coordinate(old_coordinates, old_object_set)

        object_set = self.objects_by_coords.get(new_coordinates)
        if not object_set:
            object_set = set()
            self.objects_by_coords[new_coordinates] = object_set
        object_set.add(game_object)
        self.reset_walkable_for_coordinate(new_coordinates, object_set)

    def call_on_tile_change(self):
        for callback in self.on_tile_change_callbacks:
            callback()

    def reset_walkable_for_coordinate(self, coordinate, object_set=None, tile=None):
        if object_set is None:
            object_set = self.get_objects_by_coordinates(coordinate)

        if tile is None:
            tile = self.get_tile(coordinate)
            if tile is None:
                return

        if tile.blocking:
            walkable = False
        else:
            walkable = False if any(
                game_object.blocking
                for game_object in object_set
            ) else True

        self.set_inner_walkable(coordinate, walkable)

    def flip_coordinate(self, coordinates):
        x, y = coordinates
        return y, x

    def set_inner_walkable(self, coordinate, walkable):
        coordinate = self.flip_coordinate(coordinate)
        self.inner_map.walkable[coordinate] = walkable

    def set_inner_transparent(self, coordinate, transparent):
        coordinate = self.flip_coordinate(coordinate)
        self.inner_map.transparent[coordinate] = transparent

    def is_coordinate_in_bounds(self, coordinate):
        x, y = coordinate
        if self.max_x > x > 0 and self.max_y > y > 0:
            return True
        return False

    def add_room(self, room):
        self.rooms.append(room)
        for x in range(0, room.width):
            for y in range(0, room.height):
                self.room_grid[(room.x + x), (room.y + y)] = room

    @property
    def width(self):
        return self.max_x

    @property
    def height(self):
        return self.max_y
