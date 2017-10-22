from core.components.base import Component


class Ammunition(Component):
    NAME = "ammunition"

    def __init__(self, ammunition_type, ammunition_damage):
        super().__init__()
        self.ammunition_type = ammunition_type
        self.ammunition_damage = ammunition_damage

    def copy(self):
        return Ammunition(self.ammunition_type, self.ammunition_damage)
