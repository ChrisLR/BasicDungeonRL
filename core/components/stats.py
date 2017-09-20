from core.components.base import Component
from bflib.characters.abilityscores import \
    Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, AbilityScoreSet
import copy


class CharacterStats(Component):
    NAME = 'stats'
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

    @property
    def strength(self):
        modifiers = self.registered_modifiers[Strength]
        return self.base_ability_score_set.strength + sum(modifiers)

    @property
    def dexterity(self):
        modifiers = self.registered_modifiers[Dexterity]
        return self.base_ability_score_set.dexterity + sum(modifiers)

    @property
    def constitution(self):
        modifiers = self.registered_modifiers[Constitution]
        return self.base_ability_score_set.constitution + sum(modifiers)

    @property
    def intelligence(self):
        modifiers = self.registered_modifiers[Intelligence]
        return self.base_ability_score_set.intelligence + sum(modifiers)

    @property
    def wisdom(self):
        modifiers = self.registered_modifiers[Wisdom]
        return self.base_ability_score_set.wisdom + sum(modifiers)

    @property
    def charisma(self):
        modifiers = self.registered_modifiers[Charisma]
        return self.base_ability_score_set.charisma + sum(modifiers)

    def register_modifier(self, ability_score):
        self.registered_modifiers[type(ability_score)].append(ability_score)

    def unregister_modifier(self, ability_score):
        self.registered_modifiers[type(ability_score)].remove(ability_score)

    def copy(self):
        return CharacterStats(copy.copy(self.base_ability_score_set))
