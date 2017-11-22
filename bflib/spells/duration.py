class SpellDuration(object):
    __slots__ = ["base_duration", "duration_per_level"]

    def __init__(self, base_duration=0, duration_per_level=None):
        self.base_duration = base_duration
        self.duration_per_level = duration_per_level
