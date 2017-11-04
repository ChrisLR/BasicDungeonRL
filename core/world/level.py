from core.gameobject import GameObject


class Level(GameObject):
    __slots__ = ["actors", "displays", "tiles", "max_x", "max_y", "objects_by_coords"]

    def __init__(self):
        super().__init__()
        self.actors = []
        self.displays = {}
        self.tiles = {}
        self.max_x = 0
        self.max_y = 0
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
        #
        # actor = game_object.actor
        # if actor:
        #     self.actors.append(game_object)

    def remove_object(self, game_object):
        display = game_object.display
        if display:
            self.displays[display.priority].remove(game_object)

        location = game_object.location
        if location:
            coords = location.get_local_coords()
            object_set = self.objects_by_coords.get(coords)
            if object_set:
                del object_set[game_object]

        actor = game_object.actor
        if actor:
            self.actors.remove(game_object)

    def add_tile(self, coordinates, tile):
        x, y = coordinates
        if x > self.max_x:
            self.max_x = x
        if y > self.max_y:
            self.max_y = y

        self.tiles[coordinates] = tile

    def get_tile(self, coordinates):
        tile = self.tiles.get(coordinates, None)
        return tile

    def remove_tile(self, coordinates):
        del self.tiles[coordinates]

    def get_objects_by_coordinates(self, coordinates):
        return self.objects_by_coords.get(coordinates, None)

    def adjust_coordinates_for_object(self, game_object, new_coordinates):
        old_coordinates = game_object.location.get_local_coords()
        if old_coordinates in self.objects_by_coords:
            del self.objects_by_coords[old_coordinates]

        object_set = self.objects_by_coords.get(new_coordinates)
        if not object_set:
            object_set = set()
            self.objects_by_coords[new_coordinates] = object_set
        object_set.add(game_object)
