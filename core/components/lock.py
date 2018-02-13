from core.components.base import Component


class Lock(Component):
    NAME = "lock"
    __slots__ = ["locked", "key"]

    def __init__(self, locked=True, key=None):
        super().__init__()
        self.locked = locked
        self.key = key

    def copy(self):
        return Lock(self.locked, self.key)
