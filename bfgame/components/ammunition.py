from core.components import Component, listing


@listing.register
class Ammunition(Component):
    NAME = "ammunition"
    __slots__ = ['ammunition_type', 'ammunition_damage']

    def __init__(self, ammunition_type, ammunition_damage):
        super().__init__()
        self.ammunition_type = ammunition_type
        self.ammunition_damage = ammunition_damage

    def copy(self):
        return Ammunition(self.ammunition_type, self.ammunition_damage)
