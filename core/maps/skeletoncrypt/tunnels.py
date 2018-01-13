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
        # Direction.East: (
        #     connectors.DungeonFloorConnectorA((2, 3)),
        #     connectors.DungeonDoorConnectorA((2, 3)),
        # ),
        # Direction.West: (
        #     connectors.DungeonFloorConnectorA((0, 3)),
        #     connectors.DungeonDoorConnectorA((0, 3)),
        # ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((1, 4)),
            connectors.DungeonDoorConnectorA((1, 4)),
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
        # Direction.North: (
        #     connectors.DungeonFloorConnectorA((3, 0)),
        #     connectors.DungeonDoorConnectorA((3, 0)),
        # ),
        # Direction.South: (
        #     connectors.DungeonFloorConnectorA((3, 2)),
        #     connectors.DungeonDoorConnectorA((3, 2))
        # ),
        Direction.East: (
            connectors.DungeonFloorConnectorA((5, 1)),
            connectors.DungeonDoorConnectorA((5, 1)),
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
            connectors.DungeonFloorConnectorA((3, 0), (4, 0)),
        ),
        Direction.South: (
            connectors.DungeonFloorConnectorA((3, 5), (4, 5)),
        ),
        Direction.East: (
            connectors.DungeonFloorConnectorA((7, 2), (7, 3)),
        ),
        Direction.West: (
            connectors.DungeonFloorConnectorA((0, 2), (0, 3)),
        ),
    }
