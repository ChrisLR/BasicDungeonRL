from core.tiles.base import Tile
from core.components.display import Display
from core.util.colors import Colors


class DungeonWall(Tile):
    name = "Dungeon Wall"
    display = Display(Colors.GRAY, Colors.BLACK, "#")
