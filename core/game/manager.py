from bearlibterminal import terminal
from clubsandwich.director import DirectorLoop

from core.game.context import GameContext
from core.generators.testing import TestingGenerator
from scenes.mainmenu import MainMenuScene


class Game(object):
    def __init__(self):
        self.game_context = GameContext()
        self.running = False

    def start(self):
        loop = MainLoop(MainMenuScene(self.game_context))
        loop.run()

    def new_game(self):
        level = TestingGenerator.generate()
        TestingGenerator.place_player(level, self.game_context.player)
        self.running = True


class MainLoop(DirectorLoop):
    def __init__(self, scene):
        super().__init__()
        self.scene = scene

    def get_initial_scene(self):
        return self.scene

    def terminal_init(self):
        super().terminal_init()
        terminal.set("window: title='BasicDungeonRL', size=120x50;")


game = Game()
