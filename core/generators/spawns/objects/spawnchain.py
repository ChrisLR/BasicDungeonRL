class SpawnChain(object):
    """
    This object allows to Spawn multiple objects with a single chance.
    """
    __slots__ = ["percent", "spawn_sets"]

    def __init__(self, percent, spawn_sets):
        self.percent = percent
        self.spawn_sets = spawn_sets

    def to_tuple_list(self):
        return [(spawn_set.spawn_type, spawn_set.spawn_point) for spawn_set in self.spawn_sets]