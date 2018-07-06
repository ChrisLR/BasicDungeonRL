from core import components
from core.generators.base import DesignPieceGenerator
from core.generators.spawns import MapPieceSpawn
from core.maps.goblincamp import huts
from core.tiles import floors, stairs
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

    @classmethod
    def place_stairs(cls, game, level):
        pos = (10, 10)
        stairs_down = stairs.WoodenStairsDown(game)
        stairs_down.register_component(components.Exit.create_down())
        tile = level.get_tile(pos)
        