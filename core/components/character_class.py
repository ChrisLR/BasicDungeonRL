from core.components import Component


class CharacterClass(Component):
    NAME = 'character_class'

    def __init__(self, *base_classes):
        super().__init__()
        self.base_classes = base_classes

    def copy(self):
        return CharacterClass(
            type(*self.base_classes)()
        )
