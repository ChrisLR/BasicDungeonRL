from bearlibterminal import terminal
from clubsandwich.director import DirectorLoop

import ui
from bfgame import abilities, actions, attacks, factories, generators
from bfgame.actionmapping import ActionMapping
from bfgame.displaypriority import DisplayPriority
from bfgame.outfits.outfitter import OutfitterService
from bfgame.util.gametime import GameTime
from scenes.charactercreation import (
    ClassSelection, AttributeSelection, RaceSelection, SkillsSelection
)
from scenes.mainmenu import MainMenuScene
from scenes.game.scene import GameScene
from scenes.manager import SceneManager
from services.echo import EchoService


class Game(object):
    def __init__(self):
        self.action_stack = None
        self.abilities = abilities.Facade(self)
        self.attacks = attacks.Facade(self)
        self.actions = actions.Facade(self)
        self.game_time = GameTime()
        self.camera = None
        self.echo = EchoService(self)
        self.game_scene = None
        self.director = None
        self.running = False
        self.factory = factories.Facade(self)
        self.ui = ui
        self.player = None
        self.outfit = OutfitterService(self)
        self.action_mapping = ActionMapping(self)

    def start(self, scene_manager=None):
        if self.director is None:
            self.player = self.factory.get("character").create_blank_player()
            self.director = MainLoop(self, scene_manager)
            self.director.run()

    def new_game(self):
        self.factory.get('character').finalize_character(self.player)
        # generator = generators.TestingGenerator
        generator = generators.GoblinCampGenerator(self)
        # generator = generators.SkeletonCrypt
        # generator = generators.WarzoneGenerator(self)
        level = generator.generate()
        self.player.display.priority = DisplayPriority.Player
        generator.place_player(level, self.player)
        self.player.vision.update_field_of_vision()
        self.running = True


class MainLoop(DirectorLoop):
    def __init__(self, game, scene_manager):
        super().__init__()
        if scene_manager is None:
            scene_manager = SceneManager(
                self, game, [
                    MainMenuScene,
                    AttributeSelection,
                    RaceSelection,
                    ClassSelection,
                    SkillsSelection,
                    GameScene,
                ])
            scene_manager.register_transition_callback(
                GameScene,
                game.new_game
            )
        self.scene_manager = scene_manager

    def get_initial_scene(self):
        return self.scene_manager.prepare_initial_scene()

    def terminal_init(self):
        super().terminal_init()
        terminal.set("window: title='BasicDungeonRL', size=120x50;")
