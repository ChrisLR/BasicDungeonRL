from core.components.base import Component


class SavingThrows(Component):
    NAME = "saving_throws"

    def __init__(self, saving_throws_set):
        super().__init__()
        self.saving_throws_set = saving_throws_set

    def copy(self):
        return SavingThrows(self.saving_throws_set)
