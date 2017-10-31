
from core.generators.maps.base import MapPiece
from core.tiles import floors, doors, walls
from core.generators import spawns
from bflib.monsters.humanoids.goblins import Goblin


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
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(100, Goblin, spawns.SpawnPoint(2, 2)),
        )
    ]


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
