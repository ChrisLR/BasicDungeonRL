from core.components import Component, listing


@listing.register
class SpawnInfo(Component):
    NAME = "spawn_info"
    __slots__ = ["appearing_set"]

    def __init__(self, appearing_set):
        super().__init__()
        self.appearing_set = appearing_set

    def copy(self):
        return SpawnInfo(self.appearing_set)
