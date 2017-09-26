from core.components.base import Component
from bflib import attacks
from bflib.tables.attackbonus import AttackBonusTable


class Combat(Component):
    NAME = "combat"

    def __init__(self):
        super().__init__()

    @property
    def attack_sets(self):
        """
        This returns the possible attack sets/chains for an object.
        :return: List of attack sets/chains
        """
        # TODO These should be component queries
        attack_sets = []
        if self.host.equipment:
            attack_sets.append(
                attacks.AttackSet(
                    attacks.WeaponAttack, amount=len(self.host.equipment.wield_locations)
                )
            )

        if self.host.monster:
            attack_sets.extend(
                self.host.monster.base_monster.attack_sets
            )

        return attack_sets

    @property
    def attack_bonus(self):
        level = 1
        if self.host.experience_pool:
            level = self.host.experience_pool.level

        if self.host.character_class:
            class_attack_bonus = self.host.character_class.base_class.level_table.get(level).attack_bonus
            return class_attack_bonus

        return AttackBonusTable.get_by_hit_dice(self.host.health.total_hit_dice_value)

    @property
    def armor_class(self):
        total_armor_class = 0
        if self.host.monster:
            total_armor_class += self.host.monster.base_monster.base_armor_class

        if self.host.equipment:
            total_armor_class += self.host.equipment.get_total_armor_class()

        return total_armor_class

    def copy(self):
        return Combat()

