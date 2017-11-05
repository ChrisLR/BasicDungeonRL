from core.components.base import Component


class Openable(Component):
    NAME = "openable"
    __slots__ = ["closed"]

    def __init__(self, closed=True):
        super().__init__()
        self.closed = closed

    def open(self):
        self.closed = False

    def close(self):
        self.closed = True

    def copy(self):
        return Openable(self.closed)
