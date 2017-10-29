from core.generators.maps.base import MapPiece
from core.tiles import floors, doors, walls


class GoblinHut1(MapPiece):
    name = "Goblin Hut 1"
    tiles = "......\n" \
            ".####.\n" \
            ".#,,#.\n" \
            ".#++#.\n" \
            "......\n"
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }
    spawn_ratios = (

    )


class GoblinHut2(MapPiece):
    name = "Goblin Hut 2"
    tiles = "......\n" \
            ".####.\n" \
            ".#,,+.\n" \
            ".####.\n" \
            "......\n"
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }


class GoblinHut3(MapPiece):
    name = "Goblin Hut 3"
    tiles = "......\n" \
            ".#++#.\n" \
            ".#,,#.\n" \
            ".####.\n" \
            "......\n"
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }


class GoblinHut4(MapPiece):
    name = "Goblin Hut 4"
    tiles = "......\n" \
            ".####.\n" \
            ".+,,#.\n" \
            ".####.\n" \
            "......\n"
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }


class GrassyClearing(MapPiece):
    name = "Grassy Clearing"
    tiles = "......\n" \
            "......\n" \
            "......\n" \
            "......\n" \
            "......\n"
    symbolic_links = {
        ".": floors.Grass,
    }
