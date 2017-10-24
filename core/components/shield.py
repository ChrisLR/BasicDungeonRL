from core.components.base import Component


class Shield(Component):
    NAME = "shield"
    __slots__ = ["shield_armor_class_melee", "shield_armor_class_missile"]

    def __init__(self, shield_armor_class_melee, shield_armor_class_missile):
        super().__init__()
        self.shield_armor_class_melee = shield_armor_class_melee
        self.shield_armor_class_missile = shield_armor_class_missile

    def copy(self):
        return Shield(self.shield_armor_class_melee, self.shield_armor_class_missile)
