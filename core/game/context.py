from core.util.gametime import GameTime


class GameContext(object):
    def __init__(self):
        self.game = None
        self.player = None
        self.game_time = GameTime()
        self.action_stack = None
        self.camera = None
        self.game_scene = None
