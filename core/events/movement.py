from core.events.base import Event


class Moved(Event):
    name = "Moved"
    __slots__ = "actor"

    def __init__(self, actor):
        self.actor = actor
