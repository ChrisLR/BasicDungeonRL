from bfgame.components.base import Component


class Openable(Component):
    NAME = "openable"
    __slots__ = ["closed", "on_state_change_callback"]

    def __init__(self, closed=True, on_state_change_callback=None):
        super().__init__()
        self.closed = closed
        self.on_state_change_callback = on_state_change_callback

    def open(self):
        lock = self.host.lock
        if lock and lock.locked:
            return False

        self.closed = False
        self.call_state_change()

        return True

    def close(self):
        if self.closed is False:
            self.closed = True
            self.call_state_change()

    def call_state_change(self):
        if self.on_state_change_callback:
            self.on_state_change_callback(self.closed)

    def copy(self):
        return Openable(self.closed)
