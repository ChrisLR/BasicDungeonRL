from bflib import items
from bflib.monsters.humanoids.goblins import Goblin
from core.generators import spawns
from core.maps.base import MapPiece
from core.tiles import floors, doors, walls


class GoblinHut1(MapPiece):
    name = "Goblin Hut 1"
    tiles = [
        "......",
        ".####.",
        ".#,,#.",
        ".#++#.",
        "......"
    ]
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
    tiles = [
        "......",
        ".####.",
        ".#,,+.",
        ".####.",
        "......",
    ]
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(100, Goblin, spawns.SpawnPoint(3, 2)),
        )
    ]


class GoblinHut3(MapPiece):
    name = "Goblin Hut 3"
    tiles = [
        "......",
        ".#++#.",
        ".#,,#.",
        ".####.",
        "......",
    ]
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(100, Goblin, spawns.SpawnPoint(3, 2)),
        )
    ]


class GoblinHut4(MapPiece):
    name = "Goblin Hut 4"
    tiles = [
        "......",
        ".####.",
        ".+,,#.",
        ".####.",
        "......"
    ]
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(100, Goblin, spawns.SpawnPoint(3, 2)),
        )
    ]


class GrassyClearing(MapPiece):
    name = "Grassy Clearing"
    tiles = [
        "......",
        "......",
        "......",
        "......",
        "......",
    ]
    symbolic_links = {
        ".": floors.Grass,
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(100, Goblin, spawns.SpawnPoint(3, 3)),
        )
    ]


class LargeHut(MapPiece):
    name = "Large Hut"
    tiles = [
        "........",
        "..####..",
        ".##,,##.",
        ".#,,,,+.",
        ".##,,##.",
        "..####..",
        "........"
    ]
    symbolic_links = {
        "#": walls.WoodenWall,
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(25, Goblin, spawns.SpawnPoint(2, 3)),
            spawns.SpawnSet(25, Goblin, spawns.SpawnPoint(3, 2)),
            spawns.SpawnSet(25, Goblin, spawns.SpawnPoint(3, 4)),
            spawns.SpawnSet(100, items.Spear, spawns.SpawnPoint(4, 2))
        )
    ]
