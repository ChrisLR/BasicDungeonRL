from core.components.base import Component


class Corpse(Component):
    NAME = 'corpse'
    __slots__ = ["base_character"]
    """
    This is the component that implements experience pools
    """

    def __init__(self, base_character):
        super().__init__()
        self.base_character = base_character

    def copy(self):
        return Corpse(self.base_character.copy())
