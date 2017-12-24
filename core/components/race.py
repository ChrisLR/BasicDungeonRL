from core.components import Component


class Race(Component):
    NAME = 'race'
    __slots__ = ["base_race"]

    def __init__(self, base_race):
        super().__init__()
        self.base_race = base_race

    @property
    def name(self):
        return self.base_race.name

    def copy(self):
        return Race(
            type(self.base_race)()
        )
