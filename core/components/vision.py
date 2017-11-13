import tdl

from core.components import Component


class Vision(Component):
    NAME = 'vision'
    __slots__ = ["fov", "fov_range"]

    def __init__(self, fov_range=3):
        super().__init__()
        self.fov = None
        self.fov_range = fov_range

    def round_update(self):
        self.update_field_of_vision()

    def copy(self):
        return Vision()

    def update_field_of_vision(self):
        x, y = self.host.location.get_local_coords()
        self.fov = tdl.map.quick_fov(x, y, self.is_transparent, 'basic', radius=self.fov_range)

    def is_transparent(self, x, y):
        if x <= 0 or y <= 0:
            return False

        tile = self.host.location.level.get_tile((x, y))
        if tile and tile.opaque:
            return False
        return True
