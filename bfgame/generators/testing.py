from bflib import items
from bflib.monsters import animals
from bfgame import components, traps
from bfgame.tiles import floors, walls
from core import components as core_components, dialog
from core.world import Level


class TestingGenerator(object):
    def __init__(self, game):
        self.game = game

    def generate(self):
        level = Level(self.game, 50, 50)
        for x in range(0, 25):
            for y in range(0, 25):
                if x == 0 or y == 0 or x == 24 or y == 24:
                    level.add_tile((x, y), walls.DungeonWall)
                else:
                    level.add_tile((x, y), floors.DungeonFloor)

        self.place_monster(level)
        self.place_magic_chest(level)
        self.place_trapped_floor(level)

        return level

    def place_player(self, level, player):
        player.location.level = level
        player.location.set_local_coords((12, 12))
        level.add_object(player)

    def place_magic_chest(self, level):
        chest = self.game.factory.route(items.Chest)
        chest.location.set_local_coords((13, 13))
        level.add_object(chest)
        chest.container.add_item(self.game.factory.route(items.Longsword))

    def place_monster(self, level):
        monster = self.game.factory.route(animals.Deer)
        monster.location.level = level
        monster.location.set_local_coords((14, 14))
        dialog_node_4 = dialog.DialogNode("Do you need any help?", "Yes! Kill the spider", on_select=self.place_spiders)
        dialog_node_3 = dialog.DialogNode("Indeed", "Glad to hear we agree")
        dialog_node_2 = dialog.DialogNode("Uh?", "Didn't you hear? I said BBBBBBBBBBBB")
        dialog_node = dialog.DialogNode("Hello", "Bbbbbbbbbbbbbb", [dialog_node_2, dialog_node_3, dialog_node_4])

        dialog_tree = dialog.DialogTree("deer", [dialog_node])
        monster.register_component(core_components.Dialog(dialog_tree))

        monster.vision.fov_range = 0
        level.add_object(monster)

    def place_spiders(self):
        player = self.game.player
        monster = self.game.factory.route(animals.GiantBlackWidow)
        level = player.location.level
        monster.location.level = level
        monster.location.set_local_coords((10, 10))
        level.add_object(monster)
        self.game.echo.player(player, "A giant spider poofs into existence nearby!")

    def place_trapped_floor(self, level):
        tile = level.get_tile((22, 22))
        tile.register_component(components.Trap(traps.Arrow))
