from bflib.skills.base import Skill
from bflib.characters import abilityscores


# TODO Mostly placeholder, each Knowledge should be its own Skill
class Knowledge(Skill):
    name = "Knowledge"
    related_stat = abilityscores.Intelligence
    natural = False
