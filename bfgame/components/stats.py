import copy

from bflib.characters.abilityscores import (
    Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, AbilityScoreSet)
from bflib.characters.abilityscores.base import AbilityScore
from core.components import Component, listing


@listing.register
class CharacterStats(Component):
    NAME = 'stats'
    __slots__ = ["base_ability_score_set", "registered_modifiers"]
    """
    This is the component that implements AbilityScores
    """

    def __init__(self, base_ability_score_set=None):
        super().__init__()
        self.base_ability_score_set = base_ability_score_set if base_ability_score_set else AbilityScoreSet()
        self.registered_modifiers = {
            Strength: [],
            Dexterity: [],
            Constitution: [],
            Intelligence: [],
            Wisdom: [],
            Charisma: [],
        }
        self._stat_mapping = {
            Strength: self.strength,
            Dexterity: self.dexterity,
            Constitution: self.constitution,
            Intelligence: self.intelligence,
            Wisdom: self.wisdom,
            Charisma: self.charisma,
        }
        self._stat_modifier_mapping = {
            Strength: self.strength_modifier,
            Dexterity: self.dexterity_modifier,
            Constitution: self.constitution_modifier,
            Intelligence: self.intelligence_modifier,
            Wisdom: self.wisdom_modifier,
            Charisma: self.charisma_modifier,
        }

    @property
    def strength(self):
        modifiers = self.registered_modifiers[Strength]
        return self.base_ability_score_set.strength.value + sum(modifiers)

    @property
    def strength_modifier(self):
        modifiers = self.registered_modifiers[Strength]
        return self.base_ability_score_set.strength.modifier(sum(modifiers))

    @property
    def dexterity(self):
        modifiers = self.registered_modifiers[Dexterity]
        return self.base_ability_score_set.dexterity.value + sum(modifiers)

    @property
    def dexterity_modifier(self):
        modifiers = self.registered_modifiers[Dexterity]
        return self.base_ability_score_set.dexterity.modifier(sum(modifiers))

    @property
    def constitution(self):
        modifiers = self.registered_modifiers[Constitution]
        return self.base_ability_score_set.constitution.value + sum(modifiers)

    @property
    def constitution_modifier(self):
        modifiers = self.registered_modifiers[Constitution]
        return self.base_ability_score_set.constitution.modifier(sum(modifiers))

    @property
    def intelligence(self):
        modifiers = self.registered_modifiers[Intelligence]
        return self.base_ability_score_set.intelligence.value + sum(modifiers)

    @property
    def intelligence_modifier(self):
        modifiers = self.registered_modifiers[Intelligence]
        return self.base_ability_score_set.intelligence.modifier(sum(modifiers))

    @property
    def wisdom(self):
        modifiers = self.registered_modifiers[Wisdom]
        return self.base_ability_score_set.wisdom.value + sum(modifiers)

    @property
    def wisdom_modifier(self):
        modifiers = self.registered_modifiers[Wisdom]
        return self.base_ability_score_set.wisdom.modifier(sum(modifiers))

    @property
    def charisma(self):
        modifiers = self.registered_modifiers[Charisma]
        return self.base_ability_score_set.charisma.value + sum(modifiers)

    @property
    def charisma_modifier(self):
        modifiers = self.registered_modifiers[Charisma]
        return self.base_ability_score_set.charisma.modifier(sum(modifiers))

    def get_modifier(self, stat):
        if isinstance(stat, AbilityScore):
            return self._stat_modifier_mapping.get(type(stat), 0)
        return self._stat_modifier_mapping.get(stat, 0)

    def register_modifier(self, ability_score):
        self.registered_modifiers[type(ability_score)].append(ability_score)

    def unregister_modifier(self, ability_score):
        self.registered_modifiers[type(ability_score)].remove(ability_score)

    def copy(self):
        return CharacterStats(copy.copy(self.base_ability_score_set))
