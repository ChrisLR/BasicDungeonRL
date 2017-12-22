from core.generators.maps.base import MapPiece
from core.tiles import floors, doors, walls


class VerticalTunnel(MapPiece):
    name = "Vertical Tunnel"
    tiles = "####\n" \
            "#..#\n" \
            "#..#\n" \
            "#..#\n" \
            "#..#\n"\
            "#..#\n" \
            "#..#\n" \
            "####\n"
    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }


class HorizontalTunnel(MapPiece):
    name = "Horizontal Tunnel"
    tiles = "########\n" \
            "#......#\n" \
            "#......#\n" \
            "########\n" \

    symbolic_links = {
        ".": floors.DungeonFloor,
        "#": walls.DungeonWall,
    }


class FourPointTunnel(MapPiece):
    name = "FourPoint Tunnel"
    tiles = "########\n" \
            "###..###\n" \
            "##....##\n" \
            "#......#\n" \
            "##....##\n" \
            "###..###\n" \
            "########\n" \

    symbolic_links = {
                ".": floors.DungeonFloor,
                "#": walls.DungeonWall,
            }
