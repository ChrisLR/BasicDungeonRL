from core.direction import Direction
from core.generators.maps.base import MapPiece
from core.generators.maps.skeletoncrypt import connectors
from core.tiles import floors, walls


class VerticalTunnel(MapPiece):
    name = "Vertical Tunnel"
    tiles = "#.#\n" \
            "#.#\n" \
            "#.#\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }
    connectors = {
        Direction.North: (
            connectors.DungeonFloorConnectorA((1, 0)),
            connectors.DungeonDoorConnectorA((1, 0)),
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((1, 2)),
            connectors.DungeonDoorConnectorA((1, 2)),
        ),
    }


class HorizontalTunnel(MapPiece):
    name = "Horizontal Tunnel"
    tiles = "###\n" \
            "...\n" \
            "###\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.East: (
            connectors.DungeonFloorConnectorA((2, 1)),
            connectors.DungeonDoorConnectorA((2, 1)),
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA((0, 1)),
            connectors.DungeonDoorConnectorA((0, 1))
        ),
    }


class FourPointTunnel(MapPiece):
    name = "FourPoint Tunnel"
    tiles = "###..###\n" \
            "........\n" \
            "###..###\n" \

    symbolic_links = {
                ".": floors.DungeonFloor,
                "#": walls.DungeonWall,
            }

    connectors = {
        Direction.North: (
            connectors.DungeonFloorConnectorA((3, 0), (4, 0)),
            connectors.DungeonDoorConnectorA((3, 0), (4, 0)),
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((3, 2), (4, 2)),
            connectors.DungeonDoorConnectorA((3, 2), (4, 2)),
        ),
        Direction.East: (
            connectors.DungeonFloorConnectorA((7, 1)),
            connectors.DungeonDoorConnectorA((7, 1)),
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA((1, 0)),
            connectors.DungeonDoorConnectorA((1, 0)),
        ),
    }
