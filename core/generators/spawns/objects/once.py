import random

from core.factories.router import route_to_factory
from core.generators.spawns.objects.spawnchain import SpawnChain


class OnceSpawner(object):
    """
    A Spawner that spawns only ONE set.
    """
    __slots__ = ["spawns"]

    def __init__(self, *spawns):
        self.spawns = spawns  # type: list

    def spawn(self, offset_coords):
        selected_set = self.select_spawn()
        return self.spawn_set(selected_set, offset_coords)

    def select_spawn(self):
        randomized_spawns = list(self.spawns)
        random.shuffle(randomized_spawns)

        for spawn_set in randomized_spawns:
            if random.randrange(1, 100) <= spawn_set.percent:
                return spawn_set

    @staticmethod
    def spawn_set(spawn_set, offset_coords):
        spawn_tuples = []
        spawned_objects = []
        if isinstance(spawn_set, SpawnChain):
            spawn_tuples.extend(spawn_set.to_tuple_list())
        else:
            if spawn_set is None:
                return []
            spawn_tuples.append((spawn_set.spawn_type, spawn_set.spawn_point))

        for spawn_type, spawn_point in spawn_tuples:
            spawn_x, spawn_y = spawn_point
            offset_x, offset_y = offset_coords
            new_spawn_point = (spawn_x + offset_x, spawn_y + offset_y)
            spawned_object = route_to_factory(spawn_type)
            spawned_object.location.set_local_coords(new_spawn_point)
            spawned_objects.append(spawned_object)

        return spawned_objects