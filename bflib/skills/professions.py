from bflib.skills.base import Skill
from bflib.characters import abilityscores


# TODO Mostly placeholder, each Profession should be its own Skill
class Profession(Skill):
    name = "Profession"
    related_stat = abilityscores.Intelligence
    natural = False
