from bearlibterminal import terminal
from clubsandwich.director import DirectorLoop

from core.displaypriority import DisplayPriority
from core.game.context import GameContext
from core import generators


class Game(object):
    def __init__(self):
        self.game_context = GameContext()
        self.game_context.game = self
        self.loop = None
        self.running = False

    def start(self):
        from scenes.mainmenu import MainMenuScene
        self.loop = MainLoop(MainMenuScene(self.game_context))
        self.loop.run()

    def new_game(self):
        # generator = generators.TestingGenerator
        # generator = generators.GoblinCampGenerator
        generator = generators.SkeletonCrypt
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


game = Game()
