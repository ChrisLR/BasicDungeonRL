from core.components import listing, Component
from core.direction import Direction


@listing.register
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
    def create_up(cls, level, exit_tile):
        """When going Up"""
        exits = {Direction.Up: (level, exit_tile)}
        return cls(exits)

    @classmethod
    def create_down(cls, level, exit_tile):
        """When going Down"""
        exits = {Direction.Down: (level, exit_tile)}
        return cls(exits)

    @classmethod
    def create_enter(cls, level, exit_tile):
        """When using Either Up or Down"""
        exits = {
            Direction.Up: (level, exit_tile),
            Direction.Down: (level, exit_tile)
        }
        return cls(exits)

    @classmethod
    def create_step(cls, level, exit_tile):
        """When stepping in the host tile"""
        # TODO Needs to register a listener for a Stepped on Event
        pass
