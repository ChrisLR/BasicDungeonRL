from core.components.base import Component


class Melee(Component):
    NAME = "melee"
    __slots__ = ["melee_damage"]

    def __init__(self, melee_damage):
        super().__init__()
        self.melee_damage = melee_damage

    def copy(self):
        return Melee(self.melee_damage)
