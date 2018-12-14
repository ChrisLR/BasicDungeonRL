from bfgame.components import Openable
from core.gameobject import GameObject


class Tile(GameObject):
    name = ""
    blocking = True
    opaque = True
    display = None

    def __init__(self, game):
        super().__init__(game=game, blocking=self.blocking, name=self.name)
        self.content = []

    def add_content(self, game_object):
        self.content.append(game_object)

    def remove_content(self, game_object):
        self.content.remove(game_object)


class Door(Tile):
    name = ""
    blocking = False
    opaque = True
    display = None
    closed_ascii = "+"
    opened_ascii = "-"

    def state_change(self, closed):
        if closed:
            self.blocking = True
            self.opaque = True
            self.display.ascii_character = self.closed_ascii
        else:
            self.blocking = False
            self.opaque = False
            self.display.ascii_character = self.opened_ascii

    def __init__(self, game, closed=True):
        super().__init__(game)
        self.register_component(Openable(closed, on_state_change_callback=self.state_change))
        self.display = self.display.copy()


class Floor(Tile):
    pass


class Stairs(Tile):
    pass


class Wall(Tile):
    pass