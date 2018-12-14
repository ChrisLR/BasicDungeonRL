from bfgame.components.base import Component


class Melee(Component):
    NAME = "melee"
    __slots__ = ["melee_damage", "weapon_type"]

    def __init__(self, melee_damage, weapon_type):
        super().__init__()
        self.weapon_type = weapon_type
        self.melee_damage = melee_damage

    def copy(self):
        return Melee(self.melee_damage, self.weapon_type)
