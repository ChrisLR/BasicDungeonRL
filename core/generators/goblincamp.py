from core.generators.base import DesignPieceGenerator
from core.generators.maps.goblincamp import huts
from core.tiles import floors
from core.world.level import Level


class GoblinCampGenerator(DesignPieceGenerator):
    filler_tile = floors.Grass
    pieces_with_percentage = [
        (50, huts.GoblinHut1),
        (50, huts.GoblinHut2),
        (50, huts.GoblinHut3),
        (50, huts.GoblinHut4),
        (100, huts.GrassyClearing),
        (50, huts.LargeHut),
    ]

    @classmethod
    def generate(cls):
        level = Level(20, 20)
        super()._generate(level)
        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((1, 1))
        level.add_object(player)
