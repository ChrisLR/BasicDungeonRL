from core.gameobject import GameObject


class Level(GameObject):
    __slots__ = ["actors", "displays", "tiles"]

    def __init__(self):
        super().__init__()
        self.actors = []
        self.displays = []
        self.tiles = {}

    def add_object(self, game_object):
        display = game_object.display
        if display:
            self.displays.append(display)

        actor = game_object.actor
        if actor:
            self.actors.append(actor)

    def remove_object(self, game_object):
        display = game_object.display
        if display:
            self.displays.remove(display)

        actor = game_object.actor
        if actor:
            self.actors.remove(actor)

    def add_tile(self, coordinates, tile):
        self.tiles[coordinates] = tile

    def get_tile(self, coordinates):
        tile = self.tiles.get(coordinates, None)
        return tile

    def remove_tile(self, coordinates):
        del self.tiles[coordinates]
