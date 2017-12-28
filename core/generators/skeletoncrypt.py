from core.generators.base import DesignPieceGenerator
from core.generators.maps.skeletoncrypt import arena, tunnels
from core.tiles import walls
from core.world.level import Level


class SkeletonCrypt(DesignPieceGenerator):
    filler_tile = walls.DungeonWall
    pieces_with_percentage = [
        (25, arena.Arena)
    ]

    @classmethod
    def generate(cls):
        level = Level(50, 50)
        generated_pieces = super()._generate(level)
        cls._make_tunnels(level, generated_pieces)
        return level

    @classmethod
    def _get_room_center(cls, piece, coordinate):
        ox, oy = coordinate
        center_y = ox + int(piece.get_height() / 2)
        center_x = oy + int(piece.get_width() / 2)

        return center_x, center_y

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((1, 1))
        level.add_object(player)
