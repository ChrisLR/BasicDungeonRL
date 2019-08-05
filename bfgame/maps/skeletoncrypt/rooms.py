from core.direction import Direction
from core.maps.base import MapPiece
from bfgame.maps.skeletoncrypt import connectors
from bfgame.tiles import floors, walls


dungeon_symbolic_link = {
    ".": floors.DungeonFloor,
    "#": walls.DungeonWall,
}


def get_base_connectors(tiles):
    """
    Places basic connectors for rooms,
    single door or double door, using the middle
    :param tiles: The tiles to evaluate
    :return: The Connector Dict
    """
    height = len(tiles) - 1
    width = max((len(row) for row in tiles)) - 1
    center_width = int(width / 2)
    center_height = int(height / 2)
    return {
        Direction.North: (
            connectors.DungeonSingleDoor((center_width, 0)),
            connectors.DungeonDoubleDoor(
                (center_width, 0),
                (center_width + 1, 0)
            ),
        ),
        Direction.South: (
            connectors.DungeonSingleDoor((center_width, height)),
            connectors.DungeonDoubleDoor(
                (center_width, height),
                (center_width + 1, height)
            ),
        ),
        Direction.East: (
            connectors.DungeonSingleDoor((width, center_height)),
            connectors.DungeonDoubleDoor(
                (width, center_height),
                (width + 1, center_height),
            ),
        ),
        Direction.West: (
            connectors.DungeonSingleDoor((0, center_height)),
            connectors.DungeonDoubleDoor(
                (0, center_height),
                (0, center_height),
            ),
        )
    }


class SimpleRoom3x3(MapPiece):
    name = "Simple Room 3x3"
    tiles = [
        "#####",
        "#...#",
        "#...#",
        "#...#",
        "#####"
    ]

    symbolic_links = dungeon_symbolic_link
    connectors = get_base_connectors(tiles)


class SimpleRoom4x4(MapPiece):
    name = "Simple Room 4x4"
    tiles = [
        "######",
        "#....#",
        "#....#",
        "#....#",
        "#....#",
        "######"
    ]

    symbolic_links = dungeon_symbolic_link
    connectors = get_base_connectors(tiles)


class SimpleRoom5x5(MapPiece):
    name = "Simple Room 5x5"
    tiles = [
        "#######",
        "#.....#",
        "#.....#",
        "#.....#",
        "#.....#",
        "#.....#",
        "#######"
    ]
    symbolic_links = dungeon_symbolic_link
    connectors = get_base_connectors(tiles)


class SmallCircularRoom(MapPiece):
    name = "Small Circular Room"
    tiles = [
        "#####",
        "##.##",
        "#...#",
        "#...#",
        "##.##",
        "#####"
    ]
    symbolic_links = dungeon_symbolic_link
    connectors = get_base_connectors(tiles)


class MediumCircularRoom(MapPiece):
    name = "Medium Circular Room"
    tiles = [
        "######",
        "##..##",
        "#....#",
        "#....#",
        "##..##",
        "#####"
    ]
    symbolic_links = dungeon_symbolic_link
    connectors = get_base_connectors(tiles)


class LargeCircularRoom(MapPiece):
    name = "Large Circular Room"
    tiles = [
        "#######",
        "##...##",
        "#.....#",
        "#.....#",
        "##...##",
        "#######"
    ]
    symbolic_links = dungeon_symbolic_link
    connectors = get_base_connectors(tiles)
