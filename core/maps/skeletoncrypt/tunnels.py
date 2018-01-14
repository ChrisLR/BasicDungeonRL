from core.direction import Direction
from core.maps.base.mappiece import MapPiece
from core.maps.skeletoncrypt import connectors
from core.tiles import floors, walls


class SingleVerticalTunnel(MapPiece):
    name = "Single Vertical Tunnel"
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
            connectors.DungeonSingleFloor((1, 0)),
            connectors.DungeonSingleDoor((1, 0)),
        ),
        Direction.South: (
            connectors.DungeonSingleFloor((1, 4)),
            connectors.DungeonSingleDoor((1, 4)),
        ),
    }


class DoubleVerticalTunnel(MapPiece):
    name = "Double Vertical Tunnel"
    tiles = "####\n" \
            "#..#\n" \
            "#..#\n" \
            "#..#\n" \
            "####\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }
    connectors = {
        Direction.North: (
            connectors.DungeonDoubleFloor((1, 0), (2, 0)),
            connectors.DungeonDoubleDoor((1, 0), (2, 0)),
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
            connectors.DungeonDoubleFloor((1, 4), (2, 4)),
            connectors.DungeonDoubleDoor((1, 4), (2, 4)),
        ),
    }


class SingleHorizontalTunnel(MapPiece):
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
            connectors.DungeonSingleFloor((5, 1)),
            connectors.DungeonSingleDoor((5, 1)),
        ),
        Direction.West: (
            connectors.DungeonSingleFloor((0, 1)),
            connectors.DungeonSingleDoor((0, 1))
        ),
    }


class DoubleHorizontalTunnel(MapPiece):
    name = "Double Horizontal Tunnel"
    tiles = "######\n" \
            "#....#\n" \
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
            connectors.DungeonDoubleFloor((5, 1), (5, 2)),
            connectors.DungeonDoubleDoor((5, 1), (5, 2)),
        ),
        Direction.West: (
            connectors.DungeonDoubleFloor((0, 1), (0, 2)),
            connectors.DungeonDoubleDoor((0, 1), (0, 2))
        ),
    }


class DoubleFourPointTunnel(MapPiece):
    name = "Double FourPoint Tunnel"
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
            connectors.DungeonDoubleFloor((3, 0), (4, 0)),
            connectors.DungeonDoubleDoor((3, 0), (4, 0)),
        ),
        Direction.South: (
            connectors.DungeonDoubleFloor((3, 5), (4, 5)),
            connectors.DungeonDoubleDoor((3, 5), (4, 5)),
        ),
        Direction.East: (
            connectors.DungeonDoubleFloor((7, 2), (7, 3)),
            connectors.DungeonDoubleDoor((7, 2), (7, 3)),
        ),
        Direction.West: (
            connectors.DungeonDoubleFloor((0, 2), (0, 3)),
            connectors.DungeonDoubleDoor((0, 2), (0, 3)),
        ),
    }


class SingleFourPointTunnel(MapPiece):
    name = "Single FourPoint Tunnel"
    tiles = "#######\n" \
            "###.###\n" \
            "#.....#\n" \
            "###.###\n" \
            "#######\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.North: (
            connectors.DungeonSingleFloor((3, 0)),
            connectors.DungeonSingleDoor((3, 0)),
        ),
        Direction.South: (
            connectors.DungeonSingleFloor((3, 4)),
            connectors.DungeonSingleDoor((3, 4)),
        ),
        Direction.East: (
            connectors.DungeonSingleFloor((6, 2)),
            connectors.DungeonSingleDoor((6, 2)),
        ),
        Direction.West: (
            connectors.DungeonSingleFloor((0, 2)),
            connectors.DungeonSingleDoor((0, 2)),
        ),
    }


class WestDoubleToEastSingleHorizontalTunnel(MapPiece):
    name = "West Double to East Horizontal Tunnel"
    tiles = "######\n" \
            "#....#\n" \
            "#..###\n" \
            "######\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.East: (
            connectors.DungeonSingleFloor((5, 1)),
            connectors.DungeonSingleDoor((5, 1)),
        ),
        Direction.West: (
            connectors.DungeonDoubleFloor((0, 1), (0, 2)),
            connectors.DungeonDoubleDoor((0, 1), (0, 2))
        ),
    }


class EastDoubleToWestSingleHorizontalTunnel(MapPiece):
    name = "East Double to West Horizontal Tunnel"
    tiles = "######\n" \
            "#....#\n" \
            "###..#\n" \
            "######\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.East: (
            connectors.DungeonDoubleFloor((5, 1), (5, 2)),
            connectors.DungeonDoubleDoor((5, 1), (5, 2)),
        ),
        Direction.West: (
            connectors.DungeonSingleFloor((0, 1)),
            connectors.DungeonSingleDoor((0, 1))
        ),
    }


class NorthDoubleToSouthSingleVerticalTunnel(MapPiece):
    name = "North Double To South Single Vertical Tunnel"
    tiles = "####\n" \
            "#..#\n" \
            "#.##\n" \
            "#.##\n" \
            "####\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.North: (
            connectors.DungeonDoubleFloor((1, 0), (2, 0)),
            connectors.DungeonDoubleDoor((1, 0), (2, 0)),
        ),
        Direction.South: (
            connectors.DungeonSingleFloor((1, 4)),
            connectors.DungeonSingleDoor((1, 4)),
        ),
    }


class SouthDoubleToNorthSingleVerticalTunnel(MapPiece):
    name = "South Double To North Single Vertical Tunnel"
    tiles = "####\n" \
            "#.##\n" \
            "#.##\n" \
            "#..#\n" \
            "####\n"

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }

    connectors = {
        Direction.North: (
            connectors.DungeonSingleFloor((1, 0)),
            connectors.DungeonSingleDoor((1, 0)),
        ),
        Direction.South: (
            connectors.DungeonDoubleFloor((1, 4), (2, 4)),
            connectors.DungeonDoubleDoor((1, 4), (2, 4)),
        ),
    }
