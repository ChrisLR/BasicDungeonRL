from core.components import Component, listing


@listing.register
class Shield(Component):
    NAME = "shield"
    __slots__ = ["armor_class_melee", "armor_class_missile"]

    def __init__(self, armor_class_melee, armor_class_missile):
        super().__init__()
        self.armor_class_melee = armor_class_melee
        self.armor_class_missile = armor_class_missile

    def copy(self):
        return Shield(self.armor_class_melee, self.armor_class_missile)
