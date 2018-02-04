from core.components.base import Component
from bflib.characters import specialabilities
from services import echo


class Experience(Component):
    NAME = 'experience'
    __slots__ = ["experience_pools", "level"]
    """
    This is the component that implements experience pools
    """

    def __init__(self, character_classes, starting_level=1):
        super().__init__()
        self.level_tables = [character_class.level_table for character_class in character_classes]
        if starting_level is 1:
            # Default starting level applies the Minimal level (For negative levels)
            starting_level = min((level_table.min for level_table in self.level_tables))

        starting_experience = min((level_table.get(starting_level).experience_required
                                   for level_table in self.level_tables))
        self.experience = starting_experience
        self.level = starting_level

    def add_experience(self, points):
        responses = self.host.query.special_ability(specialabilities.ExperienceBonus)
        percent_bonus = sum((int(response) for response in responses))
        points += round(((points * percent_bonus) / 100))
        self.experience += points
        exp_for_next_level = self.exp_for_next_level
        if exp_for_next_level is not None:
            if self.experience > self.exp_for_next_level:
                self.level_up()

    def level_up(self):
        self.level += 1
        if echo.is_player(self.host):
            echo.echo_service.echo("You advance to level {}".format(self.level))
        self.host.health.on_level_up()

    def copy(self):
        new = Experience(self.experience_pools.copy())
        new.level = self.level
        return new

    @property
    def current_exp(self):
        return self.experience

    @property
    def exp_for_next_level(self):
        next_levels = (level_table.get(self.level + 1) for level_table in self.level_tables)
        if any(level.experience_required for level in next_levels):
            return sum((level.experience_required
                        for level in next_levels if level))
        return None
