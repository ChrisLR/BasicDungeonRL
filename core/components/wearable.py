from core.components.base import Component


class Wearable(Component):
    NAME = "wearable"

    def __init__(self, wear_locations):
        super().__init__()
        self.wear_locations = wear_locations

    def copy(self):
        return Wearable(self.wear_locations)
