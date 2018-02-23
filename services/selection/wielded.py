from services.selection.base import Selection


class Wielded(Selection):
    def resolve(self):
        self.resolution = [item for item in self.executor.equipment.get_wielded_items()]
