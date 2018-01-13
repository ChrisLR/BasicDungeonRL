from core.generators.base import ConnectorBasedGenerator
from core.generators.spawns import MapPieceSpawn
from core.maps.skeletoncrypt import tunnels, arena, cells
from core.generators import spawns
from core.tiles import floors
from core.world.level import Level


class SkeletonCrypt(ConnectorBasedGenerator):
    filler_tile = floors.WoodenFloor
    pieces = [
        #MapPieceSpawn(25, arena.Arena, spawn_limit=1),
        MapPieceSpawn(100, tunnels.FourPointTunnel),
        MapPieceSpawn(50, tunnels.HorizontalTunnel),
        MapPieceSpawn(50, tunnels.VerticalTunnel),
        #MapPieceSpawn(25, cells.LargeCellArea, spawn_limit=1),
    ]
    max_amount_of_rooms = 1

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
