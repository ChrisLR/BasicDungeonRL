from core.components.base import Component


class Inventory(Component):
    NAME = "inventory"
    __slots__ = []

    def __init__(self):
        super().__init__()

    def add(self, item):
        if self.host.equipment:
            containers = (item for item in self.host.equipment.get_all_items() if item.container)
            for container in containers:
                if container.add(item):
                    return True

        return False

    def remove(self, item):
        if self.host.equipment:
            containers = (item for item in self.host.equipment.get_all_items() if item.container)
            for container in containers:
                if container.remove(item):
                    return True

        return False

    def copy(self):
        return Inventory()
