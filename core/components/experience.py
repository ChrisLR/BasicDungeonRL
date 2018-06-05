from bflib.characters import specialabilities
from core.components.base import Component
from services import echo


class Experience(Component):
    NAME = 'experience'
    __slots__ = ["experience_pools", "level"]
    """
    This is the component that implements experience pools
    """

    def __init__(self, character_classes, starting_level=1):
        super().__init__()
        self.level_tables = [
            character_class.level_table
            for character_class in character_classes]
        if starting_level is 1:
            # Default starting level applies the Minimal level (For negative levels)
            starting_level = min((level_table.min for level_table in self.level_tables))

        starting_experience = min((level_table.get(starting_level).experience_required
                                   for level_table in self.level_tables))
        self.experience = starting_experience
        self.level = starting_level

    def evaluate_level_tables(self):
        character_classes = self.host.character_class.base_classes
        self.level_tables = [character_class.level_table
                             for character_class in character_classes]

    def add_experience(self, points):
        percent_bonus = self.host.query.special_ability(specialabilities.ExperienceBonus)
        points += round(((points * percent_bonus) / 100))
        self.experience += points
        exp_for_next_level = self.exp_for_next_level
        if exp_for_next_level is not None:
            if self.level == 0 and self.experience >= 0:
                self.add_new_class()
                # Level up will be called by the action
                return

            if self.experience >= self.exp_for_next_level:
                self.level_up()
        else:
            if self.level == 0:
                self.add_new_class()

    def level_up(self):
        self.level += 1
        self.host.echo.player(self.host, "You advance to level {}".format(self.level))
        self.host.health.on_level_up()
        skills = self.host.skills
        if skills:
            skills.skill_points += 3

    def add_new_class(self):
        # This means we were in negative levels and must choose
        # A new class

        # TODO Each GameObject needs its own ActionStack
        add_class_action = self.host.game.actions.get("add_class")
        self.host.game.action_stack.add_action_to_stack(add_class_action)
        return

    def copy(self):
        new = Experience(self.experience_pools.copy())
        new.level = self.level
        return new

    @property
    def current_exp(self):
        return self.experience

    @property
    def exp_for_next_level(self):
        next_levels = (level_table.get(self.level + 1)
                       for level_table in self.level_tables)
        required_experience = [
            level.experience_required
            for level in next_levels
            if level.experience_required is not None
        ]
        if required_experience:
            return sum(required_experience)
        return None

    @property
    def effective_level(self):
        """
        This include the lowest negative level
        """
        lowest = min([level_table.min for level_table in self.level_tables])
        if lowest == 1:
            return self.level
        elif lowest == 0:
            return self.level + 1
        elif lowest <= -1:
            return self.level + (lowest * -1) + 1
        return self.level
