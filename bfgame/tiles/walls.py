from bfgame.components.display import Display
from bfgame.tiles.base import Tile
from bfgame.util.colors import Colors


class Wall(Tile):
    pass


class DungeonWall(Wall):
    name = "Dungeon Wall"
    display = Display(Colors.GRAY, Colors.BLACK, "#")


class WoodenWall(Wall):
    name = "Wooden Wall"
    display = Display(Colors.BROWN, Colors.BLACK, "#")
