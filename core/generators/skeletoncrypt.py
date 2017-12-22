from core.generators.base import DesignPieceGenerator
from core.generators.maps.skeletoncrypt import arena, tunnels
from core.tiles import walls
from core.world.level import Level


class SkeletonCrypt(DesignPieceGenerator):
    filler_tile = walls.DungeonWall
    pieces_with_percentage = [
        (25, arena.Arena),
        (25, tunnels.FourPointTunnel)
    ]

    @classmethod
    def generate(cls):
        level = Level(50, 50)
        super()._generate(level)
        cls._make_tunnels(level)
        return level

    @classmethod
    def _make_tunnels(cls, level):
        pass

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((1, 1))
        level.add_object(player)
