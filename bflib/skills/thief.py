from bflib.characters import abilityscores
from bflib.characters.classes import Thief
from bflib.skills import listing
from bflib.skills.base import Skill


@listing.register
class Balance(Skill):
    name = "Balance"
    related_stat = abilityscores.Dexterity
    natural = True
    character_class = Thief


@listing.register
class Bluff(Skill):
    name = "Bluff"
    related_stat = abilityscores.Charisma
    natural = True
    character_class = Thief


@listing.register
class Disguise(Skill):
    name = "Disguise"
    related_stat = abilityscores.Charisma
    natural = True
    character_class = Thief


@listing.register
class EscapeArtist(Skill):
    name = "Escape Artist"
    related_stat = abilityscores.Dexterity
    natural = True
    character_class = Thief


@listing.register
class Forgery(Skill):
    name = "Forgery"
    related_stat = abilityscores.Intelligence
    natural = False
    character_class = Thief


@listing.register
class Tumble(Skill):
    name = "Tumble"
    related_stat = abilityscores.Dexterity
    natural = True
    character_class = Thief
