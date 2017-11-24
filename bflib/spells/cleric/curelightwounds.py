from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Instantaneous
from bflib.spells.range import Touch


@listing.register_spell
class CureLightWounds(Spell):
    name = "Cure Light Wounds"
    class_level_map = {
        classes.Cleric: 1,
    }
    duration = Instantaneous()
    range = Touch()
