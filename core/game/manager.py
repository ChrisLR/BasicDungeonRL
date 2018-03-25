from bearlibterminal import terminal
from clubsandwich.director import DirectorLoop

import ui
from core import factories, generators
from core.displaypriority import DisplayPriority
from core.util.gametime import GameTime
from scenes.mainmenu import MainMenuScene
from services.echo import EchoService


class Game(object):
    def __init__(self):
        self.game_time = GameTime()
        self.camera = None
        self.echo = EchoService(self)
        self.game_scene = None
        self.director = None
        self.running = False
        self.factory = factories.Facade(self)
        self.ui = ui
        self.player = None

    def start(self):
        if self.director is None:
            self.director = MainLoop(MainMenuScene(self))
            self.director.run()

    def new_game(self):
        # generator = generators.TestingGenerator
        generator = generators.GoblinCampGenerator
        # generator = generators.SkeletonCrypt
        level = generator.generate()
        self.player.display.priority = DisplayPriority.Player
        generator.place_player(level, self.player)

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
