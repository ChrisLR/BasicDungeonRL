from core.components.base import Component


class Armor(Component):
    NAME = "armor"
    __slots__ = ['armor_class', 'armor_type']

    def __init__(self, armor_class, armor_type):
        super().__init__()
        self.armor_class = armor_class
        self.armor_type = armor_type

    def copy(self):
        return Armor(self.armor_class, self.armor_type)
