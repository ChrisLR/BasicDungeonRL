from core.components.base import Component


class SpawnInfo(Component):
    NAME = "spawn_info"

    def __init__(self, appearing_set):
        super().__init__()
        self.appearing_set = appearing_set

    def copy(self):
        return SpawnInfo(self.appearing_set)
