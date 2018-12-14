from bfgame import components
from bfgame.maps.goblincamp import huts
from bfgame.tiles import floors, stairs
from core.generators.base import DesignPieceGenerator
from core.generators.spawns import MapPieceSpawn
from core.world import Level, LevelStub


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

    def __init__(self, game):
        self.game = game

    def generate(self):
        level = Level(self.game, 50, 50)
        super()._generate(level)
        self.place_exit_stairs_temp(self.game, level)

        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((1, 1))
        level.add_object(player)

    @classmethod
    def place_exit_stairs_temp(cls, game, level):
        from bfgame.generators.skeletoncrypt import SkeletonCrypt
        stairs_down = stairs.WoodenStairsDown(game)
        stairs_up = stairs.WoodenStairsUp(game)
        next_level_stub = LevelStub(game, SkeletonCrypt(game), stairs_up)
        previous_level_stub = LevelStub(game, cls(game))
        pos = (10, 10)

        stairs_down.register_component(components.Exit.create_down(next_level_stub, stairs_up))
        stairs_down.register_component(components.TileLocation())
        stairs_down.location.set_local_coords(pos)
        stairs_up.register_component(components.Exit.create_up(previous_level_stub, stairs_down))
        stairs_up.register_component(components.TileLocation())

        previous_level_stub._level = level

        level.add_tile(pos, stairs_down)
