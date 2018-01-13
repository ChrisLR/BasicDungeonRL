from core.direction import Direction
from core.maps.base.mappiece import MapPiece
from core.maps.skeletoncrypt import connectors
from core.tiles import floors, walls


class VerticalTunnel(MapPiece):
    name = "Vertical Tunnel"
    tiles = "###\n" \
            "#.#\n" \
            "#.#\n" \
            "#.#\n" \
            "###\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }
    connectors = {
        Direction.North: (
            connectors.DungeonFloorConnectorA((1, 0)),
            connectors.DungeonDoorConnectorA((1, 0)),
        ),
        Direction.East: (
            connectors.DungeonFloorConnectorA((2, 3)),
            connectors.DungeonDoorConnectorA((2, 3)),
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA((0, 3)),
            connectors.DungeonDoorConnectorA((0, 3)),
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((1, 2)),
            connectors.DungeonDoorConnectorA((1, 2)),
        ),
    }


class HorizontalTunnel(MapPiece):
    name = "Horizontal Tunnel"
    tiles = "######\n" \
            "#....#\n" \
            "######\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.North: (
            connectors.DungeonFloorConnectorA((3, 0)),
            connectors.DungeonDoorConnectorA((3, 0)),
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((3, 2)),
            connectors.DungeonDoorConnectorA((3, 2))
        ),
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
    tiles = "########\n" \
            "###..###\n" \
            "#......#\n" \
            "#......#\n" \
            "###..###\n" \
            "########\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.North: (
            connectors.DungeonFloorConnectorA((4, 0), (5, 0)),
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((4, 5), (5, 5)),
        ),
        Direction.East: (
            connectors.DungeonFloorConnectorA((7, 3), (7, 4)),
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA((0, 3), (0, 4)),
        ),
    }
