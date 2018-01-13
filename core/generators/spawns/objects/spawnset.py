class SpawnSet(object):
    """
    A Set Containing a Percent and a Spawn Type.
    """
    __slots__ = ["percent", "spawn_type", "spawn_point"]

    def __init__(self, percent, spawn_type, spawn_point):
        self.percent = percent
        self.spawn_type = spawn_type
        self.spawn_point = spawn_point