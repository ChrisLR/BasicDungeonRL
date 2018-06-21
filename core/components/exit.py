from core.components.base import Component


class Exit(Component):
    """
    A component that maps triggers to move an object to another level/position
    """
    NAME = "exit"
    __slots__ = ()

    def __init__(self):
        super().__init__()

    @classmethod
    def create_up(cls, level, position):
        """When going Up"""
        pass

    @classmethod
    def create_down(cls, level, position):
        """When going Down"""
        pass

    @classmethod
    def create_enter(cls, level, position):
        """When using Either Up or Down"""
        pass

    @classmethod
    def create_step(cls, level, position):
        """When stepping in the host tile"""
        pass
