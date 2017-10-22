from core.components.base import Component


class Size(Component):
    NAME = "size"

    def __init__(self, base_score):
        super().__init__()
        self.base_score = base_score

    @property
    def score(self):
        return self.base_score

    def copy(self):
        return Size(self.base_score)
