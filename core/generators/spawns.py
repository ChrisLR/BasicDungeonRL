import random
from core.factories.router import route_to_factory


class OnceSpawner(object):
    """
    A Spawner that spawns only ONE set.
    """
    __slots__ = ["spawn_sets"]

    def __init__(self, spawn_sets):
        self.spawn_sets = spawn_sets

    def spawn_objects(self):
        randomized_spawns = sorted(self.spawn_sets, key=random.randint(0, 100))
        for spawn_set in randomized_spawns:
            if random.randrange(1, 100) <= spawn_set.percent:
                return [route_to_factory(spawn_type) for spawn_type in spawn_set.spawn_types]


class SpawnSet(object):
    """
    A Set Containing a Percent and a Spawn Type.
    """
    __slots__ = ["percent", "spawn_types"]

    def __init__(self, percent, *spawn_types):
        self.percent = percent
        self.spawn_types = spawn_types
