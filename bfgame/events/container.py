from bfgame.events.base import Event


class Opened(Event):
    name = "Opened"
    __slots__ = "actor"

    def __init__(self, actor):
        self.actor = actor
