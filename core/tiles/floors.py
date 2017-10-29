from core.tiles.base import Tile
from core.components.display import Display
from core.util.colors import Colors


class DungeonFloor(Tile):
    name = "Dungeon Floor"
    display = Display(Colors.GRAY, Colors.BLACK, ".")
    blocking = False
    opaque = False


class Grass(Tile):
    name = "Grass"
    display = Display(Colors.GREEN, Colors.BLACK, ".")
    blocking = False
    opaque = False


class WoodenFloor(Tile):
    name = "Wooden Floor"
    display = Display(Colors.BROWN, Colors.BLACK, ".")
    blocking = False
    opaque = False
