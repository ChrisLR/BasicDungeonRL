from bflib import units


class CarryCapacity(object):
    __slots__ = ["light_load", "heavy_load"]

    def __init__(self, light_load, heavy_load):
        self.light_load = light_load  # type: units.Feet
        self.heavy_load = heavy_load  # type: units.Feet
