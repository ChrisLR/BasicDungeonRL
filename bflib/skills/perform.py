from bflib.skills.base import Skill
from bflib.characters import abilityscores


# TODO Mostly placeholder, each Perform should be its own Skill
class Perform(Skill):
    name = "Perform"
    related_stat = abilityscores.Charisma
    natural = False
