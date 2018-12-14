from bfgame.components.display import Display
from core.tiles.base import Wall
from core.util.colors import Colors


class DungeonWall(Wall):
    name = "Dungeon Wall"
    display = Display(Colors.GRAY, Colors.BLACK, "#")


class WoodenWall(Wall):
    name = "Wooden Wall"
    display = Display(Colors.BROWN, Colors.BLACK, "#")
