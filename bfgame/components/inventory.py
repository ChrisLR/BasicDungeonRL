from bfgame.components.base import Component
from core import contexts
from core.messaging import StringBuilder, Actor, TargetOne, TargetTwo, His, Verb


class Inventory(Component):
    NAME = "inventory"
    __slots__ = []

    def __init__(self):
        super().__init__()

    def add(self, item):
        if self.host.equipment:
            containers = (item.container for item in self.host.equipment.get_all_items() if item.container)
            for container in containers:
                if container.add_item(item):
                    message = StringBuilder(Actor, Verb("add", Actor), TargetOne, "to", His(Actor), TargetTwo)
                    context = contexts.TwoTargetAction(self.host, item, container.host)
                    self.host.game.echo.see(self.host, message, context)

                    return True

        return False

    def get_all_items(self):
        items = []
        if self.host.equipment:
            equipped_items = self.host.equipment.get_all_items()
            items.extend(equipped_items)
            containers = (item.container for item in equipped_items if item.container)
            for container in containers:
                items.extend(container.items_held)

        return items

    def get_inventory_items(self):
        items = []
        if self.host.equipment:
            equipped_items = self.host.equipment.get_all_items()
            containers = (item.container for item in equipped_items if item.container)
            for container in containers:
                self._recursive_get_container_items(container, items)

        return items

    def get_item_hierarchy(self):
        """
        Returns all items with their hierarchy, includes equipment.
        """
        item_hierarchy = {}
        if self.host.equipment:
            parent_items = self.host.equipment.get_all_items()
            for parent_item in parent_items:
                if parent_item.container:
                    item_hierarchy[parent_item] = parent_item.container.items_held
                else:
                    item_hierarchy[parent_item] = []

        return item_hierarchy

    def _recursive_get_container_items(self, container, item_list):
        containers = []
        for item in container.items_held:
            if item.container:
                containers.append(item.container)
            else:
                item_list.append(item)

        for new_container in containers:
            self._recursive_get_container_items(new_container, item_list)

    def remove(self, item):
        equipment = self.host.equipment
        if equipment:
            containers = (item.container for item in equipment.get_all_items() if item.container)
            for container in containers:
                if container.remove_item(item):
                    return True

        return False

    def copy(self):
        return Inventory()
