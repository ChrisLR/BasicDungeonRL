from core.components.base import Component


class Location(Component):
    NAME = "location"

    def __init__(self):
        super().__init__()
        self.area = None
        self.level = None
        self.local_x = 0
        self.local_y = 0
        self.region = None
        self.world_x = 0
        self.world_y = 0

    def copy(self):
        new_instance = Location()
        new_instance.area = self.area
        new_instance.level = self.level
        new_instance.local_x = self.local_x
        new_instance.local_y = self.local_y
        new_instance.region = self.region
        new_instance.world_x = self.world_x
        new_instance.world_y = self.world_y

        return new_instance

    def get_local_coords(self):
        return self.local_x, self.local_y

    def set_local_coords(self, coordinates):
        self.local_x, self.local_y = coordinates
