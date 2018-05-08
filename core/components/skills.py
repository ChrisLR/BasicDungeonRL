from bflib import dice
from core import queries
from core.components.base import Component


class Skills(Component):
    NAME = "skills"
    __slots__ = ["base_skills"]

    def __init__(self, base_skills):
        super().__init__()
        self.base_skills = base_skills or set()

    def on_register(self, host):
        super().on_register(host)
        host.query.register_responder(queries.Skills, self, self.respond_skill_value)

    def respond_skill_value(self, query):
        query.respond(self.base_skills)

    def get_increase_cost(self, skill):
        requires_class = skill.character_class
        if requires_class is not None:
            host_class = self.host.character_class
            if host_class and requires_class in host_class.base_classes:
                return 1
            return 3
        return 1

    def get_stat_bonus(self, skill):
        stat = skill.related_stat
        host_stats = self.host.stats
        if host_stats:
            return host_stats.get_modifier(stat)
        return 0

    def roll_check(self, skill):
        skill_value = self.host.query.skills(skill)
        stat_bonus = self.get_stat_bonus(skill)

        return dice.D20(1, flat_bonus=skill_value + stat_bonus).roll()

    def copy(self):
        return Skills(self.base_skills.copy())
