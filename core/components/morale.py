from core.components.base import Component


class Morale(Component):
    NAME = "morale"

    def __init__(self):
        super().__init__()
        self.cornered = False
        self.fleeing = False

    @property
    def score(self):
        morale_score = 6
        if self.host.monster:
            morale_score = self.host.monster.base_monster.morale

        return morale_score

    def copy(self):
        return Morale()

