from bflib import monsters
from core.direction import Direction
from core.generators import spawns
from core.generators.maps.base import MapPiece
from core.generators.maps.skeletoncrypt import connectors
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
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(2, 2)),
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(2, 3)),
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(3, 2)),
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(3, 3)),
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(3, 4)),
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(4, 3)),
            spawns.SpawnSet(100, monsters.Skeleton, spawns.SpawnPoint(4, 4)),
        )
    ]
    connectors = {
        Direction.North: connectors.DungeonDoorConnectorA,
        Direction.East: connectors.DungeonDoorConnectorA,
        Direction.South: connectors.DungeonDoorConnectorA,
        Direction.West: connectors.DungeonDoorConnectorA,
    }
