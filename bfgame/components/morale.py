from core.components.base import Component


class Morale(Component):
    NAME = "morale"
    __slots__ = ["base_morale", "cornered", "fleeing"]

    def __init__(self, base_morale=6):
        super().__init__()
        self.base_morale = base_morale
        self.cornered = False
        self.fleeing = False

    @property
    def score(self):
        return self.base_morale

    def copy(self):
        return Morale(self.base_morale)
