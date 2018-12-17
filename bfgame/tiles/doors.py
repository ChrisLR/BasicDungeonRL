from core.components.display import Display
from core.tiles.base import Door
from core.util.colors import Colors


class DungeonDoor(Door):
    name = "Dungeon Door"
    display = Display(Colors.GRAY, Colors.BLACK, "+")


class WoodenDoor(Door):
    name = "Wooden Door"
    display = Display(Colors.BROWN, Colors.BLACK, "+")
