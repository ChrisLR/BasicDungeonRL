from core.gameobject import GameObject


class Level(GameObject):
    __slots__ = ["displays", "tiles", "max_x", "max_y", "objects_by_coords"]

    def __init__(self, max_x, max_y):
        super().__init__()
        self.displays = {}
        self.tiles = {}
        self.max_x = max_x
        self.max_y = max_y
        self.objects_by_coords = {}

    @property
    def game_objects(self):
        game_objects = []
        for game_object_set in self.objects_by_coords.values():
            game_objects.extend(game_object_set)

        return game_objects

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

    def add_tile(self, coordinates, tile_class):
        x, y = coordinates
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        self.tiles[coordinates] = tile_class()

    def get_tile(self, coordinates):
        tile = self.tiles.get(coordinates, None)
        return tile

    def remove_tile(self, coordinates):
        del self.tiles[coordinates]

    def get_objects_by_coordinates(self, coordinates):
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
