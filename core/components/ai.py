from core.components.base import Component


class AI(Component):
    NAME = 'ai'
    __slots__ = ["personality"]
    """
    This is the component that implements experience pools
    """

    def __init__(self, personality):
        super().__init__()
        self.personality = personality

    def round_update(self):
        action = self.personality.act(self.host)
        action.execute(self.host)

    def copy(self):
        return AI(self.personality.copy())
