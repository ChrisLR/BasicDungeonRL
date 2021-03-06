from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import Touch


@listing.register_spell
class FindThePath(Spell):
    name = "Find The Path"
    class_level_map = {
        classes.Cleric: 6,
    }
    duration = SpellDuration(duration_per_level=units.GameTurn(1))
    range = Touch()
