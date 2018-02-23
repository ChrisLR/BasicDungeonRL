from services.selection.base import Selection


class EquippedSelection(Selection):
    def resolve(self):
        self.resolution = [item for item in self.executor.equipment.get_all_items()]
