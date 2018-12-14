from bfgame.components.display import Display
from bfgame.components.openable import Openable
from bfgame.tiles.base import Tile
from core.util.colors import Colors


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


class DungeonDoor(Door):
    name = "Dungeon Door"
    display = Display(Colors.GRAY, Colors.BLACK, "+")


class WoodenDoor(Door):
    name = "Wooden Door"
    display = Display(Colors.BROWN, Colors.BLACK, "+")
