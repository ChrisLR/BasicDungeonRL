from bflib.items.containers import base as base_container_types
from bfgame.components import Component


class SpecialContainer(Component):
    NAME = "specialcontainer"
    __slots__ = ["container_type", "containable_items", "items_held",
                 "max_quantity", "volume_limit", "weight_limit"]

    def __init__(self, container_type, containable_items, max_quantity):
        super().__init__()
        self.container_type = container_type
        self.containable_items = containable_items
        self.max_quantity = max_quantity

    def add_item(self, item):
        if self.container_type is base_container_types.LiquidContainer:
            return False

        if self.max_quantity:
            if len(self.items_held) >= self.max_quantity:
                return False

        if self.weight_limit:
            total_weight = self.total_weight
            if total_weight + item.weight.score > self.weight_limit:
                return False

        if self.container_type is base_container_types.Container:
            self.items_held.append(item)

        if self.container_type is base_container_types.SpecialContainer \
            and any((isinstance(item.base_type, containable_type)
                     for containable_type in self.containable_items)):
            self.items_held.append(item)

        return True

    def remove_item(self, item):
        if self.container_type is base_container_types.LiquidContainer:
            return False

        self.items_held.remove(item)
        return True

    @property
    def total_weight(self):
        return sum(item.weight.score for item in self.items_held) if self.items_held else 0

    def copy(self):
        return SpecialContainer(
            self.container_type,
            self.containable_items,
            self.max_quantity,
        )
