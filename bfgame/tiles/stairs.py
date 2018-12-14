from bfgame.components.display import Display
from core.tiles.base import Stairs
from core.util.colors import Colors


class DungeonStairsUp(Stairs):
    name = "Dungeon Stairs Up"
    display = Display(Colors.GRAY, Colors.BLACK, ">")
    blocking = False
    opaque = False


class DungeonStairsDown(Stairs):
    name = "Dungeon Stairs Down"
    display = Display(Colors.GRAY, Colors.BLACK, "<")
    blocking = False
    opaque = False


class WoodenStairsDown(Stairs):
    name = "Wooden Floor"
    display = Display(Colors.BROWN, Colors.BLACK, "<")
    blocking = False
    opaque = False


class WoodenStairsUp(Stairs):
    name = "Wooden Floor"
    display = Display(Colors.BROWN, Colors.BLACK, ">")
    blocking = False
    opaque = False
