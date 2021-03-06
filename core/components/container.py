from bflib import units
from core.components import listing, Component
from core.components.contained import Contained


@listing.register
class Container(Component):
    NAME = "container"
    __slots__ = ["container_type", "containable_items", "items_held", "liquid_held",
                 "max_quantity", "volume_limit", "weight_limit"]

    def __init__(self, container_type, volume_limit, weight_limit):
        super().__init__()
        self.container_type = container_type
        self.items_held = []
        self.volume_limit = volume_limit
        self.weight_limit = weight_limit

    def add_item(self, item):
        if self.weight_limit:
            total_weight = self.total_weight
            if item.weight:
                if total_weight + item.weight.score > self.weight_limit:
                    return False

        self.items_held.append(item)
        if item.contained:
            item.contained.parent_container.remove_item(item)
            item.contained.parent_container = self
        else:
            item.register_component(Contained(self))

        return True

    def remove_item(self, item):
        if item in self.items_held:
            self.items_held.remove(item)
            item.unregister_component(Contained(self))
            return True

        return False

    @property
    def total_weight(self):
        return sum(
            [item.weight.score for item in self.items_held if item.weight]) \
            if self.items_held else units.Pound(0)

    def copy(self):
        return Container(
            self.container_type,
            self.volume_limit,
            self.weight_limit
        )
