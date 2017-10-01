from bflib.monsters import animals
from core.factories.monster import MonsterFactory
from core.tiles import floors, walls
from core.world.level import Level


class TestingGenerator(object):
    @classmethod
    def generate(cls):
        level = Level()
        for x in range(0, 50):
            for y in range(0, 50):
                if x == 0 or y == 0 or x == 49 or y == 49:
                    level.add_tile((x, y), walls.DungeonWall)
                else:
                    level.add_tile((x, y), floors.DungeonFloor)

        cls.place_monster(level)
        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.level = level
        player.location.set_local_coords((24, 24))
        level.add_object(player)

    @classmethod
    def place_monster(cls, level):
        monster = MonsterFactory.create_new(animals.Deer)
        monster.location.level = level
        monster.location.set_local_coords((23, 23))
        level.add_object(monster)
