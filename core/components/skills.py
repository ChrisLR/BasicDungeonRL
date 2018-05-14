from bflib import dice
from core import queries
from core.components.base import Component


class Skills(Component):
    NAME = "skills"
    __slots__ = ["base_skills"]

    def __init__(self, base_skills=None):
        super().__init__()
        self.base_skills = base_skills or {}
        self.skill_points = 0

    def on_register(self, host):
        super().on_register(host)
        host.query.register_responder(queries.Skills, self, self.respond_skill_value)

    def decrease_skill(self, skill_type, points=1):
        current = self.base_skills.get(skill_type)
        if current is not None:
            current.value -= points
            if current.value <= 0:
                current.value = 0

    def increase_skill(self, skill_type, points=1):
        current = self.base_skills.get(skill_type)
        if current is not None:
            current.value += points
        else:
            new = skill_type(points)
            self.base_skills[type(new)] = new

    def set_skill(self, skill_type, value):
        self.base_skills[skill_type] = skill_type(value)

    def respond_skill_value(self, query):
        query.respond(self.base_skills.values())

    def get_increase_cost(self, skill_type):
        requires_class = skill_type.character_class
        if requires_class is not None:
            host_class = self.host.character_class
            if host_class and requires_class in host_class.base_classes:
                return 1
            return 3
        return 1

    def get_stat_bonus(self, skill_type):
        stat = skill_type.related_stat
        host_stats = self.host.stats
        if host_stats:
            return host_stats.get_modifier(stat)
        return 0

    def get_base_skill_value(self, skill_type):
        base_skill = self.base_skills.get(skill_type)
        if base_skill is not None:
            return base_skill.value
        return 0

    def get_skill_value(self, skill_type):
        return self.host.query.skills(skill_type)

    def roll_check(self, skill_type):
        skill_value = self.get_skill_value(skill_type)
        stat_bonus = self.get_stat_bonus(skill_type)

        return dice.D20(1, flat_bonus=skill_value + stat_bonus).roll()

    def copy(self):
        return Skills(self.base_skills.copy())
