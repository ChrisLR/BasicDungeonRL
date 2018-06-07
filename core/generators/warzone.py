from bflib import items
from bflib.monsters import humanoids
from core import components, traps
from core.tiles import floors, walls
from core.world.level import Level
import random


class WarzoneGenerator(object):
    """A Generator to test alliances"""
    def __init__(self, game):
        self.game = game
        self.monster_factory = game.factory.get('monster')

    def generate(self):
        level = Level(self.game, 50, 50)
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


    def place_allies(self, level):
        pass

    def place_enemies(self, level):
        orcs = [self.monster_factory.create_new(humanoids.Orc)]