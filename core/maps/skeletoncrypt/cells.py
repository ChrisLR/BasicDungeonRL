from bflib import monsters
from core.direction import Direction
from core.generators import spawns
from core.maps.base import MapPiece
from core.maps.skeletoncrypt import connectors
from core.tiles import floors, doors, walls


class LargeCellArea(MapPiece):
    name = "Large Cell Area"
    tiles = [
        "#########",
        "#.#.#.#.#",
        "#+#+#+#+#",
        "#.......#",
        "#.......#",
        "#+#+#+#+#",
        "#.#.#.#.#",
        "#########",
    ]
    symbolic_links = {
        ".": floors.DungeonFloor,
        "+": doors.DungeonDoor,
        "#": walls.DungeonWall,
    }
    spawners = [
        spawns.OnceSpawner(
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(4, 4)),
        )
    ]
    connectors = {
        Direction.West: (
            connectors.DungeonDoubleDoor((0, 3), (0, 4)),
            connectors.DungeonSingleDoor((0, 3)),
        ),
        Direction.East: (
            connectors.DungeonDoubleDoor((8, 3), (8, 4)),
            connectors.DungeonSingleDoor((8, 3)),
        ),
    }
