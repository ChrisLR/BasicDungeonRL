from bflib import items
from bflib.monsters import animals
from core import components, traps
from core.factories.monster import MonsterFactory
from core.tiles import floors, walls
from core.world.level import Level


class TestingGenerator(object):
    def __init__(self, game):
        self.game = game

    def generate(self):
        level = Level(100, 100)
        for x in range(0, 50):
            for y in range(0, 50):
                if x == 0 or y == 0 or x == 49 or y == 49:
                    level.add_tile((x, y), walls.DungeonWall)
                else:
                    level.add_tile((x, y), floors.DungeonFloor)

        self.place_monster(level)
        self.place_magic_chest(level)
        self.place_trapped_floor(level)

        return level

    def place_player(self, level, player):
        player.location.level = level
        player.location.set_local_coords((24, 24))
        level.add_object(player)

    def place_magic_chest(self, level):
        chest = self.game.factory.route(items.Chest)
        chest.location.set_local_coords((25, 25))
        chest.register_component(components.Trap(traps.Arrow))
        level.add_object(chest)
        chest.container.add_item(self.game.factory.route(items.Longsword))

    def place_monster(self, level):
        monster = self.game.factory.route(animals.Deer)
        monster.location.level = level
        monster.location.set_local_coords((23, 23))
        monster.register_component(components.Openable())
        monster.register_component(components.Lock())
        monster.register_component(components.Container(None, None, None))
        monster.register_component(components.Trap(traps.Arrow))
        monster.vision.fov_range = 0
        level.add_object(monster)

    def place_trapped_floor(self, level):
        tile = level.get_tile((22, 22))
        tile.register_component(components.Trap(traps.Arrow))
