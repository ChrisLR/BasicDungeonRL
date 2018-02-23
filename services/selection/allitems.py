from services.selection.base import Selection


class AllItems(Selection):
    def resolve(self):
        self.resolution = [item for item in self.executor.inventory.get_all_items()]
