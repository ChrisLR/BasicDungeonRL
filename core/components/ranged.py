from core.components.base import Component


class Ranged(Component):
    NAME = "ranged"
    __slots__ = ["range_set", "ammunition_type"]

    def __init__(self, range_set, ammunition_type):
        super().__init__()
        self.range_set = range_set
        self.ammunition_type = ammunition_type

    def copy(self):
        return Ranged(self.range_set, self.ammunition_type)
