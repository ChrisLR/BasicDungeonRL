from core.components import Component, listing


@listing.register
class Size(Component):
    NAME = "size"
    __slots__ = ["base_score"]

    def __init__(self, base_score):
        super().__init__()
        self.base_score = base_score

    @property
    def score(self):
        return self.base_score

    def copy(self):
        return Size(self.base_score)
