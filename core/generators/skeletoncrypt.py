from core.generators.base import ConnectorBasedGenerator
from core.generators.spawns import MapPieceSpawn
from core.maps.skeletoncrypt import tunnels, arena, cells, rooms
from core.generators import spawns
from core.tiles import walls
from core.world.level import Level


class SkeletonCrypt(ConnectorBasedGenerator):
    filler_tile = walls.DungeonWall
    pieces = [
        MapPieceSpawn(20, arena.Arena, spawn_limit=1),
        MapPieceSpawn(20, tunnels.DoubleFourPointTunnel),
        MapPieceSpawn(10, tunnels.SingleHorizontalTunnel),
        MapPieceSpawn(10, tunnels.SingleVerticalTunnel),
        MapPieceSpawn(10, tunnels.SingleFourPointTunnel),
        MapPieceSpawn(20, tunnels.DoubleHorizontalTunnel),
        MapPieceSpawn(20, tunnels.DoubleVerticalTunnel),
        MapPieceSpawn(20, cells.LargeCellArea, spawn_limit=1),
        MapPieceSpawn(30, rooms.SimpleRoom3x3),
        MapPieceSpawn(30, rooms.SimpleRoom4x4),
        MapPieceSpawn(30, rooms.SimpleRoom5x5),
        MapPieceSpawn(30, rooms.SmallCircularRoom),
        MapPieceSpawn(30, rooms.MediumCircularRoom),
        MapPieceSpawn(30, rooms.LargeCircularRoom),
    ]
    max_amount_of_rooms = 50

    @classmethod
    def generate(cls):
        level = Level(50, 50)
        super()._generate(level)

        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        first_room = level.rooms[0]
        coordinate = spawns.get_unoccupied_position(
            level=level,
            origin_x=first_room.x,
            origin_y=first_room.y,
            width=first_room.width,
            height=first_room.height,
        )
        player.location.set_local_coords(coordinate)
        level.add_object(player)
