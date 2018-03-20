from bearlibterminal import terminal
from clubsandwich.director import DirectorLoop

from core import factories, generators
import services
import ui
from core.util.gametime import GameTime
from core.displaypriority import DisplayPriority
from scenes.mainmenu import MainMenuScene


class Game(object):
    def __init__(self):
        self.game_time = GameTime()
        self.camera = None
        self.game_scene = None
        self.director = None
        self.running = False
        self.factory = factories.Facade(self)
        self.service = services.Facade(self)
        self.ui = ui

    def start(self):
        if self.director is None:
            self.director = MainLoop(MainMenuScene(self))
            self.director.run()

    def new_game(self):
        # generator = generators.TestingGenerator
        generator = generators.GoblinCampGenerator
        # generator = generators.SkeletonCrypt
        level = generator.generate()
        self.game_context.player.display.priority = DisplayPriority.Player
        generator.place_player(level, self.game_context.player)

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
