from core.events.base import Event


class Attacking(Event):
    name = "Attacking"
    __slots__ = "actor"

    def __init__(self, actor):
        self.actor = actor
