from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.range import Touch


@listing.register_spell
class AnimateDead(Spell):
    name = "Animate Dead"
    class_level_map = {
        classes.Cleric: 4,
        classes.MagicUser: 5,
    }
    duration = None
    range = Touch()
