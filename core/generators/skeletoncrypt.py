import random

from core.generators.base import ConnectorBasedGenerator, DesignPieceGenerator, TunneledDesignPieceGenerator
from core.generators.maps.skeletoncrypt import arena, tunnels, cells
from core.generators import spawns
from core.tiles import floors
from core.world.level import Level


class SkeletonCrypt(TunneledDesignPieceGenerator):
    filler_tile = floors.WoodenFloor
    pieces_with_percentage = [
        (100, arena.Arena),
        (100, cells.LargeCellArea),
    ]
    max_amount_of_rooms = 3

    @classmethod
    def generate(cls):
        level = Level(50, 50)
        super()._generate(level)

        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        random_room = random.choice(level.rooms)
        coordinate = spawns.get_unoccupied_position(
            level=level,
            origin_x=random_room.x,
            origin_y=random_room.y,
            width=random_room.width,
            height=random_room.height,
        )
        player.location.set_local_coords((1, 1))
        level.add_object(player)
