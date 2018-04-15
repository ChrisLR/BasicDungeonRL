from bflib import attacks, dice
from bflib.tables.attackbonus import AttackBonusTable
from core.components.base import Component
from bflib.characters import specialabilities


class Combat(Component):
    NAME = "combat"
    __slots__ = []

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
                    attacks.WeaponAttack, amount=len(self.host.equipment.get_wielded_grasp_slots())
                )
            )

        if self.host.body:
            attack_sets.extend(self.host.body.get_attacks())

        if self.host.monster and self.host.monster.base_monster.attack_sets:
            attack_sets.extend(
                self.host.monster.base_monster.attack_sets
            )

        return attack_sets

    @property
    def attack_bonus(self):
        level = 1
        if self.host.experience:
            level = self.host.experience.level

        if self.host.character_class:
            class_attack_bonus = self.host.character_class.get_attack_bonus(level)
            return class_attack_bonus

        if self.host.monster:
            return self.host.monster.attack_bonus

        return AttackBonusTable.get_by_hit_dice(self.host.health.total_hit_dice_value)

    @property
    def armor_class(self):
        health = self.host.health
        if health and not health.conscious:
            return 0

        no_armor = 11
        total_ac = no_armor
        dexterity_bonus = self.host.stats.dexterity_modifier
        if dexterity_bonus:
            if not health or (health and health.conscious):
                total_ac += dexterity_bonus

        if self.host.monster:
            natural_armor = self.host.monster.base_armor_class - no_armor
            total_ac += natural_armor

        if self.host.equipment:
            melee_ac = self.host.equipment.get_melee_total_armor_class()
            if melee_ac > no_armor:
                melee_ac -= no_armor

            melee_defense_bonus = self.host.query.special_ability(specialabilities.MeleeDefenseBonus)
            total_ac += melee_ac + melee_defense_bonus

        if health and not health.conscious:
            total_ac -= no_armor

        return total_ac

    def copy(self):
        return Combat()
