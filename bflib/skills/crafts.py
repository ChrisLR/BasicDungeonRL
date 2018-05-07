from bflib.skills.base import Skill
from bflib.characters import abilityscores


# TODO Mostly placeholder, each craft should be its own Skill
class Craft(Skill):
    name = "Craft"
    related_stat = abilityscores.Intelligence
    natural = False
