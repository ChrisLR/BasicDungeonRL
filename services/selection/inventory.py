from services.selection.base import Selection


class Inventory(Selection):
    def resolve(self):
        self.resolution = [item for item in self.executor.inventory.get_inventory_items()]


class ChainedInventory(Selection):
    def resolve(self):
        chain = self.parent_selection_set.parent_chain
        target = chain.get("Holder").targets[0]
        if target.inventory:
            self.resolution = [item for item in target.inventory.get_inventory_items()]
