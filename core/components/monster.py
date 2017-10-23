from core.components.base import Component


class Monster(Component):
    NAME = "monster"
    __slots__ = ["base_monster"]

    def __init__(self, base_monster):
        super().__init__()
        self.base_monster = base_monster

    def copy(self):
        return Monster(self.base_monster)

