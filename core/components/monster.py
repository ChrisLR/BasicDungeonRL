from core import queries
from core.components.base import Component


class Monster(Component):
    NAME = "monster"
    __slots__ = ["base_monster"]

    def __init__(self, base_monster):
        super().__init__()
        self.base_monster = base_monster

    def on_register(self, host):
        super().on_register(host)
        host.query.register_responder(queries.Experience, self, self.respond_experience_value)

    def respond_experience_value(self, query):
        query.respond(self.base_monster.xp)

    @property
    def attack_bonus(self):
        return self.base_monster.attack_bonus

    @property
    def base_armor_class(self):
        return self.base_monster.base_armor_class

    @property
    def carry_capacity(self):
        return self.base_monster.carry_capacity

    @property
    def exp_worth(self):
        return self.base_monster.xp

    def copy(self):
        return Monster(self.base_monster)

