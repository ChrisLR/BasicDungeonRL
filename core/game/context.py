from core.actions.stack import ActionStack
from core.gameobject import GameObject
from core.util.gametime import GameTime


class GameContext(object):
    def __init__(self):
        self.game = None
        self.player = None  # type: GameObject
        self.game_time = GameTime()
        self.action_stack = None  # type: ActionStack
