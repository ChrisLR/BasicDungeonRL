from core.components.base import Component
from bflib.characters import specialabilities


class Experience(Component):
    NAME = 'experience'
    __slots__ = ["experience_pools", "level"]
    """
    This is the component that implements experience pools
    """

    def __init__(self, character_classes, starting_level=1):
        super().__init__()
        self.level_tables = [character_class.level_table for character_class in character_classes]
        self.experience = 0
        self.level = starting_level

    def add_experience(self, points):
        responses = self.host.query.special_ability(specialabilities.ExperienceBonus)
        percent_bonus = sum((int(response) for response in responses))
        points += round(((points * percent_bonus) / 100))
        self.experience += points

    def copy(self):
        new = Experience(self.experience_pools.copy())
        new.level = self.level
        return new

    @property
    def current_exp(self):
        return self.experience

    @property
    def exp_for_next_level(self):
        return sum((level_table.levels[self.level + 1].experience_required
                    for level_table in self.level_tables))
