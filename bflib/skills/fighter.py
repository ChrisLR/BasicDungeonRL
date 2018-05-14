from bflib.characters import abilityscores
from bflib.characters.classes import Fighter
from bflib.skills import listing
from bflib.skills.base import Skill


@listing.register
class Endurance(Skill):
    name = "Endurance"
    related_stat = abilityscores.Constitution
    natural = True
    character_class = Fighter


@listing.register
class Intimidate(Skill):
    name = "Intimidate"
    related_stat = abilityscores.Charisma
    natural = True
    character_class = Fighter


@listing.register
class Leadership(Skill):
    name = "Leadership"
    related_stat = abilityscores.Charisma
    natural = True
    character_class = Fighter
