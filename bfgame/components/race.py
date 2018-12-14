from bfgame.components import Component
from bfgame import queries


class Race(Component):
    NAME = 'race'
    __slots__ = ["base_race"]

    def __init__(self, base_race):
        super().__init__()
        self.base_race = base_race

    def on_register(self, host):
        super().on_register(host)
        host.query.register_responder(queries.SpecialAbility, self, self.respond_special_abilities)

    def respond_special_abilities(self, query):
        query.respond(self.base_race.special_ability_set.special_abilities)

    @property
    def name(self):
        return self.base_race.name

    def copy(self):
        return Race(
            type(self.base_race)()
        )
