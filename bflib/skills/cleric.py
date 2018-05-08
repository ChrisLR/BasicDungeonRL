from bflib.characters import abilityscores
from bflib.characters.classes import Cleric
from bflib.skills import listing
from bflib.skills.base import Skill


@listing.register
class Ceremony(Skill):
    name = "Ceremony"
    related_stat = abilityscores.Wisdom
    natural = False
    character_class = Cleric


@listing.register
class DivineSpellcraft():
    name = "Divine Spellcraft"
    related_stat = abilityscores.Intelligence
    natural = False
    character_class = Cleric


@listing.register
class Heal(Skill):
    name = "Heal"
    related_stat = abilityscores.Wisdom
    natural = False
    character_class = Cleric
