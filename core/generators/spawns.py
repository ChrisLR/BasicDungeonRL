class OnceSpawner(object):
    """
    A Spawner that spawns only ONE set.
    """
    def __init__(self, spawn_sets):
        self.spawn_sets = spawn_sets

    def spawn_objects(self):
        pass


class SpawnSet(object):
    """
    A Set Containing a Percent and a Spawn Type.
    """
    def __init__(self, percent, spawn_type):
        pass