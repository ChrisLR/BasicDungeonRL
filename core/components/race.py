from core.components import Component


class Race(Component):
    NAME = 'race'

    def __init__(self, base_race):
        super().__init__()
        self.base_race = base_race

    def copy(self):
        return Race(
            type(self.base_race)()
        )
