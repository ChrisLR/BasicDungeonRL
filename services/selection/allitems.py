from services.selection.base import Selection


class AllItems(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.resolution = [item for item in self.executor.inventory.get_all_items()]
