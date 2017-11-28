from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import Touch


@listing.register_spell
class Fly(Spell):
    name = "Fly"
    class_level_map = {
        classes.MagicUser: 3,
    }
    duration = SpellDuration(duration_per_level=units.GameTurn(1))
    range = Touch()
