from core.actions.base import Action
from core.direction import Direction, move_direction_mapping


class Move(Action):
    @classmethod
    def can_execute(cls, character, direction=None):
        pass

    @classmethod
    def execute(cls, character, direction=None):
        pass
