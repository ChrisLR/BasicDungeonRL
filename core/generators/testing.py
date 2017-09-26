from core.world.level import Level
from core.tiles import floors, walls


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

        return level

    @classmethod
    def place_player(cls, level, player):
        player.location.set_local_coords((24, 24))
        player.location.level = level
        level.add_object(player)
