from bflib.characters import abilityscores
from bflib.characters.classes import MagicUser
from bflib.skills import listing
from bflib.skills.base import Skill


@listing.register
class DecipherScript(Skill):
    name = "Decipher Script"
    related_stat = abilityscores.Intelligence
    natural = False
    character_class = MagicUser


@listing.register
class ArcaneSpellcraft(Skill):
    name = "Arcane Spellcraft"
    related_stat = abilityscores.Intelligence
    natural = False
    character_class = MagicUser
