from bfgame.components.base import Component


class Weight(Component):
    NAME = "weight"
    __slots__ = ["base_score"]

    def __init__(self, base_score):
        super().__init__()
        self.base_score = base_score

    @property
    def score(self):
        return self.base_score

    def copy(self):
        return Weight(self.base_score)
