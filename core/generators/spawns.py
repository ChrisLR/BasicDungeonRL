import random

from core.factories.router import route_to_factory


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


class SpawnSet(object):
    """
    A Set Containing a Percent and a Spawn Type.
    """
    __slots__ = ["percent", "spawn_type", "spawn_point"]

    def __init__(self, percent, spawn_type, spawn_point):
        self.percent = percent
        self.spawn_type = spawn_type
        self.spawn_point = spawn_point


class SpawnPoint(object):
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y


def get_unoccupied_position(level, origin_x, origin_y, width, height):
    tries = (origin_x * width) + (origin_y * height)
    while tries:
        tries -= 1
        x = random.randint(1, width) + origin_x
        y = random.randint(1, height) + origin_y
        coordinate = x, y
        tile = level.get_tile(coordinate)
        if not tile or tile.blocking:
            continue

        blocking_objects = [
            game_object for game_object
            in level.get_objects_by_coordinates(coordinate)
            if game_object.blocking]

        if blocking_objects:
            continue

        return coordinate
