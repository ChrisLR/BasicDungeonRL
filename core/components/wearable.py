from core.components import Component, listing


@listing.register
class Wearable(Component):
    NAME = "wearable"
    __slots__ = ["wear_locations"]

    def __init__(self, wear_locations):
        super().__init__()
        self.wear_locations = wear_locations

    def copy(self):
        return Wearable(self.wear_locations)
