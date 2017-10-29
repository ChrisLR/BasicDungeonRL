from core.components.display import Display
from core.tiles.base import Tile
from core.util.colors import Colors


class Door(Tile):
    name = ""
    blocking = True
    opaque = True
    display = None
    closed_ascii = "+"
    opened_ascii = "-"

    def __init__(self, opened=False):
        super().__init__()
        self.opened = opened
        self.blocking = True if not self.opened else False
        self.display.ascii_character = self.closed_ascii if not self.opened else self.opened_ascii


class DungeonDoor(Tile):
    name = "Dungeon Door"
    display = Display(Colors.GRAY, Colors.BLACK, "+")


class WoodenDoor(Tile):
    name = "Dungeon Door"
    display = Display(Colors.BROWN, Colors.BLACK, "+")
