from core.components.base import Component


class Lock(Component):
    NAME = "lock"
    __slots__ = ["difficulty", "locked", "key"]

    def __init__(self, difficulty, locked=True, key=None):
        super().__init__()
        self.difficulty = difficulty
        self.locked = locked
        self.key = key

    def copy(self):
        return Lock(self.difficulty, self.locked, self.key)
