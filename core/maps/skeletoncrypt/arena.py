from bflib import monsters
from core.direction import Direction
from core.generators import spawns
from core.maps.base import MapPiece
from core.maps.skeletoncrypt import connectors
from core.tiles import floors, doors, walls


class Arena(MapPiece):
    name = "Arena"
    tiles = "##########\n" \
            "#........#\n" \
            "#........#\n" \
            "#........#\n" \
            "#........#\n"\
            "#........#\n" \
            "#........#\n" \
            "##########\n"
    symbolic_links = {
        ".": floors.DungeonFloor,
        "+": doors.DungeonDoor,
        "#": walls.DungeonWall,
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnChain(100, spawn_sets=[
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(2, 2)),
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(2, 3)),
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(3, 2)),
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(3, 3)),
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(3, 4)),
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(4, 3)),
                spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(4, 4)),
            ])
        )
    ]
    connectors = {
        Direction.North: (
            connectors.DungeonDoorConnectorA(
                *[(x, 0) for x in range(4, 7)]
            ),
        ),
        Direction.East: (
            connectors.DungeonDoorConnectorA(
                *[(9, y) for y in range(4, 7)]
            ),
        ),
        Direction.South: (
            connectors.DungeonDoorConnectorA(
                *[(x, 7) for x in range(4, 7)]
            ),
        ),
        Direction.West: (
            connectors.DungeonDoorConnectorA(
                *[(0, y) for y in range(4, 7)]
            ),
        ),
    }
