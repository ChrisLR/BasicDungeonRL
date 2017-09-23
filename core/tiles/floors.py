from core.tiles.base import Tile
from core.components.display import Display
from core.util.colors import Colors


class DungeonFloor(Tile):
    name = "Dungeon Floor"
    display = Display(Colors.GRAY, Colors.BLACK, ".")
    blocking = False
