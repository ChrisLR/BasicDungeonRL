from core.components.base import Component


class Monster(Component):
    NAME = "monster"
    __slots__ = ["base_monster"]

    def __init__(self, base_monster):
        super().__init__()
        self.base_monster = base_monster

    @property
    def attack_bonus(self):
        return self.base_monster.attack_bonus

    @property
    def base_armor_class(self):
        return self.base_monster.base_armor_class

    @property
    def carry_capacity(self):
        return self.base_monster.carry_capacity

    @property
    def exp_worth(self):
        return self.base_monster.xp

    def copy(self):
        return Monster(self.base_monster)

