from core.components.base import Component


class AI(Component):
    NAME = 'ai'
    __slots__ = ["last_behavior", "personality"]
    """
    This is the component that implements experience pools
    """

    def __init__(self, personality):
        super().__init__()
        self.last_behavior = None
        self.personality = personality

    def round_update(self):
        behavior = self.personality.get_behavior(self.host, self.last_behavior)
        if behavior:
            action = behavior.get_action()
            if action:
                action.execute(self.host)

    def copy(self):
        return AI(self.personality.copy())
