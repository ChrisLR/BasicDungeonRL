from services.selection.base import Selection


class EquippedSelection(Selection):
    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def resolve(self):
        self.resolution = [item for item in self.executor.equipment.get_all_items()]
