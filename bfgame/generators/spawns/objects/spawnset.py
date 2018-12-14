class SpawnSet(object):
    """
    A Set Containing a Percent and a Spawn Type.
    """
    __slots__ = ["amount", "percent", "spawn_type", "spawn_point"]

    def __init__(self, percent, spawn_type, spawn_point, amount=0):
        self.amount = amount
        self.percent = percent
        self.spawn_type = spawn_type
        self.spawn_point = spawn_point

    def on_spawn(self, game, spawned_object, origin):
        pass


class ContainerSpawnSet(object):
    """
    A SpawnSet containing A Percent, Spawn Type, and Child Spawner.
    This expects the parent to have a container component.
    """
    __slots__ = [
        "amount", "percent", "spawn_type",
        "spawn_point", "child_spawner"
    ]

    def __init__(self, percent, spawn_type, spawn_point,
                 child_spawner, amount=0):
        self.amount = amount
        self.percent = percent
        self.spawn_type = spawn_type
        self.spawn_point = spawn_point
        self.child_spawner = child_spawner

    def on_spawn(self, game, spawned_object, origin):
        spawned_children = self.child_spawner.spawn(game, origin)
        for children in spawned_children:
            spawned_object.container.add_item(children)
            children.location.update_from_other(spawned_object.location)
