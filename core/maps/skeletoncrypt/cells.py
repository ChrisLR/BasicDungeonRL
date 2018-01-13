from bflib import monsters
from core.direction import Direction
from core.generators import spawns
from core.maps.base import MapPiece
from core.maps.skeletoncrypt import connectors
from core.tiles import floors, doors, walls


class LargeCellArea(MapPiece):
    name = "Large Cell Area"
    tiles = "#########\n" \
            "#.#.#.#.#\n" \
            "#+#+#+#+#\n" \
            "#.......#\n" \
            "#.......#\n" \
            "#+#+#+#+#\n" \
            "#.#.#.#.#\n" \
            "#########\n"
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
        Direction.East: (
            connectors.DungeonDoorConnectorA(
                (0, 4), (0, 5)
            ),
        ),
        Direction.West: (
            connectors.DungeonDoorConnectorA(
                (8, 4), (8, 5)
            ),
        ),
    }
