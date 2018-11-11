import random

from core.generators.spawns.objects.spawnchain import SpawnChain


class OnceSpawner(object):
    """
    A Spawner that spawns only ONE set.
    """
    __slots__ = ["spawns"]

    def __init__(self, *spawns):
        self.spawns = spawns  # type: list

    def spawn(self, game, origin):
        selected_set = self.select_spawn()
        return self.spawn_set(game, selected_set, origin)

    def select_spawn(self):
        randomized_spawns = list(self.spawns)
        random.shuffle(randomized_spawns)

        for spawn_set in randomized_spawns:
            if random.randrange(1, 100) <= spawn_set.percent:
                return spawn_set

    @classmethod
    def spawn_set(cls, game, spawn_set, origin):
        if spawn_set is None:
            return []

        spawn_sets = []
        spawned_objects = []
        if isinstance(spawn_set, SpawnChain):
            cls.expand_spawn_chains(spawn_set, spawn_sets)
        else:
            spawn_sets.append(spawn_set)

        for spawn_set in spawn_sets:
            spawn_x, spawn_y = spawn_set.spawn_point
            offset_x, offset_y = origin
            new_spawn_point = (spawn_x + offset_x, spawn_y + offset_y)
            if spawn_set.amount:
                for _ in range(spawn_set.amount):
                    spawned_objects.append(game.factory.route(spawn_set.spawn_type))
            else:
                spawned_objects.append(game.factory.route(spawn_set.spawn_type))

            for spawned_object in spawned_objects:
                spawned_object.location.set_local_coords(new_spawn_point)
                spawn_set.on_spawn(game, spawned_object, origin)

        return spawned_objects

    @classmethod
    def expand_spawn_chains(cls, spawn_chain, spawn_sets):
        for spawn_set in spawn_chain.spawn_sets:
            if isinstance(spawn_set, SpawnChain):
                cls.expand_spawn_chains(spawn_set, spawn_sets)
            else:
                spawn_sets.append(spawn_set)
