from core.components.base import Component
from core.direction import Direction


class Exit(Component):
    """
    A component that maps triggers to move an object to another level/position
    """
    NAME = "exit"
    __slots__ = ()

    def __init__(self, exits=None):
        super().__init__()
        self.exits = exits or {}

    def get_exit(self, direction):
        return self.exits.get(direction)

    @classmethod
    def create_up(cls, level, position):
        """When going Up"""
        exits = {Direction.Up: (level, position)}
        return cls(exits)

    @classmethod
    def create_down(cls, level, position):
        """When going Down"""
        exits = {Direction.Down: (level, position)}
        return cls(exits)

    @classmethod
    def create_enter(cls, level, position):
        """When using Either Up or Down"""
        exits = {
            Direction.Up: (level, position),
            Direction.Down: (level, position)
        }
        return cls(exits)

    @classmethod
    def create_step(cls, level, position):
        """When stepping in the host tile"""
        # TODO Needs to register a listener for a Stepped on Event
        pass
