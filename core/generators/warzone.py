from bflib import items
from bflib.monsters import humanoids
from core import components, traps
from core.tiles import floors, walls
from core.world.level import Level
from core.alliances import Faction, Team
import random


class WarzoneGenerator(object):
    """A Generator to test alliances"""
    def __init__(self, game):
        self.game = game
        self.monster_factory = game.factory.get('monster')
        self.ally_faction = None

    def generate(self):
        level = Level(self.game, 50, 50)
        for x in range(0, 50):
            for y in range(0, 50):
                level.add_tile((x, y), floors.Grass)

        self.ally_faction = Faction()
        enemy_faction = Faction()
        self.ally_faction.add_enemy_faction(enemy_faction)
        enemy_faction.add_enemy_faction(self.ally_faction)

        self.place_allies(level, self.ally_faction)
        self.place_enemies(level, enemy_faction)
        self.place_neutrals(level)

        return level

    def place_player(self, level, player):
        player.location.level = level
        player.location.set_local_coords((24, 24))
        level.add_object(player)
        self.ally_faction.add_member(player)

    def place_neutrals(self, level):
        # Orcs that do not get involved
        starting_x = 20
        y = 1
        for x in range(10):
            self.build_warzone_orc(level, x + starting_x, y)

    def place_allies(self, level, ally_faction):
        # Orcs that help the player
        x = 20
        starting_y = 10
        for y in range(10):
            self.build_warzone_orc(level, x, y + starting_y, ally_faction)

    def place_enemies(self, level, enemy_faction):
        # Orcs that attack the player
        x = 40
        starting_y = 10
        for y in range(10):
            self.build_warzone_orc(level, x, y + starting_y, enemy_faction)

    def build_warzone_orc(self, level, x, y, faction=None):
        orc = self.monster_factory.create_new(humanoids.Orc)
        orc.location.level = level
        orc.location.set_local_coords((x, y))
        if faction is not None:
            faction.add_member(orc)

        return orc
