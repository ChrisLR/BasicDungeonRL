from core.components.base import Component
from services import echo


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
                    if echo.functions.is_player(self.host):
                        echo.echo_service.echo("You add {} to your {}.".format(
                            item.name, container.host.name))
                    else:
                        echo.echo_service.echo("{} adds {} to {} {}.".format(
                            self.host.name, item.name,
                            echo.functions.his_her_it(self.host),
                            container.host.name)
                        )

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

    def remove(self, item):
        if self.host.equipment:
            containers = (item.container for item in self.host.equipment.get_all_items() if item.container)
            for container in containers:
                if container.remove_item(item):
                    return True

        return False

    def copy(self):
        return Inventory()
