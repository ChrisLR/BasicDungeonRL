from bflib.characters.abilityscores import Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma


class AbilityScoreSet(object):
    __slots__ = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def __init__(self, strength=3, dexterity=3, constitution=3, intelligence=3, wisdom=3, charisma=3):
        self.strength = Strength(strength)
        self.dexterity = Dexterity(dexterity)
        self.constitution = Constitution(constitution)
        self.intelligence = Intelligence(intelligence)
        self.wisdom = Wisdom(wisdom)
        self.charisma = Charisma(charisma)

    @classmethod
    def from_merge(cls, first, other):
        return cls(
            strength=max(first.strength, other.strength),
            dexterity=max(first.dexterity, other.dexterity),
            constitution=max(first.constitution, other.constitution),
            intelligence=max(first.intelligence, other.intelligence),
            wisdom=max(first.wisdom, other.wisdom),
            charisma=max(first.charisma, other.charisma),
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
