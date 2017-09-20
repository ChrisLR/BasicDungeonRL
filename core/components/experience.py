from core.components.base import Component


class Experience(Component):
    NAME = 'experience'
    """
    This is the component that implements experience pools
    """

    def __init__(self, character_classes, starting_level=1):
        super().__init__()
        self.experience_pools = {character_class: 0 for character_class in character_classes}
        self.level = starting_level

    def copy(self):
        new = Experience(self.experience_pools.copy())
        new.level = self.level
        return new

    @property
    def current_exp(self):
        return sum(self.experience_pools.values())

    @property
    def exp_for_next_level(self):
        level_tables = (character_class.level_table for character_class in self.experience_pools.keys())
        return sum((level_table.levels[self.level].experience_required for level_table in level_tables))
