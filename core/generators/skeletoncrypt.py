import random

from core.generators.base import ConnectorBasedGenerator
from core.generators.maps.skeletoncrypt import arena, tunnels
from core.generators import spawns
from core.tiles import walls
from core.world.level import Level


class SkeletonCrypt(ConnectorBasedGenerator):
    filler_tile = walls.DungeonWall
    pieces_with_percentage = [
        #(25, arena.Arena),
        (25, tunnels.HorizontalTunnel),
        (25, tunnels.VerticalTunnel),
        (25, tunnels.FourPointTunnel),
    ]

    @classmethod
    def generate(cls):
        level = Level(50, 50)
        super()._generate(level)

        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        #random_room = random.choice(level.rooms)
        random_room = level.rooms[0]
        coordinate = spawns.get_unoccupied_position(
            level=level,
            origin_x=random_room.x,
            origin_y=random_room.y,
            width=random_room.width,
            height=random_room.height,
        )
        player.location.set_local_coords(coordinate)
        level.add_object(player)
