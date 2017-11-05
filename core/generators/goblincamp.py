from bflib.monsters import animals
from core.factories.monster import MonsterFactory
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
        level = Level()
        level.max_x = 100
        level.max_y = 100
        super()._generate(level)
        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((1, 1))
        level.add_object(player)

    @classmethod
    def place_monster(cls, level):
        monster = MonsterFactory.create_new(animals.Deer)
        monster.location.level = level
        monster.location.set_local_coords((23, 23))
        level.add_object(monster)
