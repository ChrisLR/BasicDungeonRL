from bflib.skills.base import Skill
from bflib.characters import abilityscores


# TODO Mostly placeholder, each labor should be its own Skill
class Labor(Skill):
    name = "Labor"
    related_stat = abilityscores.Intelligence
    natural = False
