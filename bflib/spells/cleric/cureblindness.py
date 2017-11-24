from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Instantaneous
from bflib.spells.range import Touch


@listing.register_spell
class CureBlindness(Spell):
    name = "Cure Blindness"
    class_level_map = {
        classes.Cleric: 3,
    }
    duration = Instantaneous()
    range = Touch()
