from core.events.base import Event


class WalkedOn(Event):
    name = "WalkedOn"
    __slots__ = "actor"

    def __init__(self, actor):
        self.actor = actor
