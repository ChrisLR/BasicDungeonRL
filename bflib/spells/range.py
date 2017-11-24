from bflib import units


class SpellRange(object):
    __slots__ = ["base_range", "range_per_level"]

    def __init__(self, base_range=None, range_per_level=None):
        self.base_range = base_range if base_range else units.Feet(0)
        self.range_per_level = range_per_level if range_per_level else units.Feet(0)


class Self(SpellRange):
    pass


class Touch(SpellRange):
    pass


class SpellRadius(SpellRange):
    __slots___ = ["base_radius", "radius_per_level"]

    def __init__(self, base_range=None, base_radius=None, range_per_level=None, radius_per_level=None):
        super().__init__(base_range, range_per_level)
        self.base_radius = base_radius if base_radius else units.Feet(0)
        self.radius_per_level = radius_per_level if radius_per_level else units.Feet(0)
