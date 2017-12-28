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
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
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
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
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
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
        ),
        Direction.East: (
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA,
            connectors.DungeonDoorConnectorA,
        ),
    }
