from core.components.display import Display
from core.tiles.base import Tile
from core.util.colors import Colors


class DungeonWall(Tile):
    name = "Dungeon Wall"
    display = Display(Colors.GRAY, Colors.BLACK, "#")


class WoodenWall(Tile):
    name = "Wooden Wall"
    display = Display(Colors.BROWN, Colors.BLACK, "#")
