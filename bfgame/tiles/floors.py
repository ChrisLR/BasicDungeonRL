from core.components.display import Display
from core.tiles.base import Floor
from core.util.colors import Colors


class DungeonFloor(Floor):
    name = "Dungeon Floor"
    display = Display(Colors.GRAY, Colors.BLACK, ".")
    blocking = False
    opaque = False


class Grass(Floor):
    name = "Grass"
    display = Display(Colors.GREEN, Colors.BLACK, ".")
    blocking = False
    opaque = False


class WoodenFloor(Floor):
    name = "Wooden Floor"
    display = Display(Colors.BROWN, Colors.BLACK, ".")
    blocking = False
    opaque = False
