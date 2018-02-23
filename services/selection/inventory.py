from services.selection.base import Selection


class Inventory(Selection):
    def resolve(self):
        self.resolution = [item for item in self.executor.inventory.get_inventory_items()]
