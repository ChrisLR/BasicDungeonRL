from bflib.characters.abilityscores import Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
from bflib.util import max_if


class AbilityScoreSet(object):
    __slots__ = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def __init__(self, strength=None, dexterity=None, constitution=None, intelligence=None, wisdom=None, charisma=None):
        self.strength = Strength(strength) if strength else None
        self.dexterity = Dexterity(dexterity) if dexterity else None
        self.constitution = Constitution(constitution) if constitution else None
        self.intelligence = Intelligence(intelligence) if intelligence else None
        self.wisdom = Wisdom(wisdom) if wisdom else None
        self.charisma = Charisma(charisma) if charisma else None

    @classmethod
    def from_merge(cls, first, other):
        return cls(
            strength=max_if(first.strength, other.strength),
            dexterity=max_if(first.dexterity, other.dexterity),
            constitution=max_if(first.constitution, other.constitution),
            intelligence=max_if(first.intelligence, other.intelligence),
            wisdom=max_if(first.wisdom, other.wisdom),
            charisma=max_if(first.charisma, other.charisma),
        )

    @classmethod
    def set_all(cls, value, **kwargs):
        return AbilityScoreSet(
            strength=kwargs.get("strength", value),
            dexterity=kwargs.get("dexterity", value),
            constitution=kwargs.get("constitution", value),
            intelligence=kwargs.get("intelligence", value),
            wisdom=kwargs.get("wisdom", value),
            charisma=kwargs.get("charisma", value)
        )
