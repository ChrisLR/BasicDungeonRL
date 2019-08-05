from bfgame.tiles import floors, doors, walls, stairs
from bflib.monsters.humanoids.goblins import Goblin
from core.generators import spawns
from core.maps.base import MapPiece


class GoblinCellar(MapPiece):
    name = "Goblin Cellar 1"
    tiles = [
        "######",
        "#....#",
        "#.<..#",
        "#....#",
        "######"
    ]
    symbolic_links = {
        ".": floors.Grass,
        ",": floors.WoodenFloor,
        "+": doors.WoodenDoor,
        "#": walls.WoodenWall
    }
    spawners = [
        spawns.OnceSpawner(
            spawns.SpawnSet(100, Goblin, spawns.SpawnPoint(3, 3)),
        )
    ]
    piece_links = {
        ">": stairs.WoodenStairsDown,
    }
