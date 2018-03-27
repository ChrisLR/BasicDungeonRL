from core.generators.base import DesignPieceGenerator
from core.generators.spawns import MapPieceSpawn
from core.maps.goblincamp import huts
from core.tiles import floors
from core.world.level import Level


class GoblinCampGenerator(DesignPieceGenerator):
    filler_tile = floors.Grass
    pieces = [
        MapPieceSpawn(50, huts.GoblinHut1),
        MapPieceSpawn(50, huts.GoblinHut2),
        MapPieceSpawn(50, huts.GoblinHut3),
        MapPieceSpawn(50, huts.GoblinHut4),
        MapPieceSpawn(100, huts.GrassyClearing),
        MapPieceSpawn(50, huts.LargeHut),
    ]

    @classmethod
    def generate(cls, game):
        level = Level(game, 50, 50)
        super()._generate(level)
        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((1, 1))
        level.add_object(player)
