from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class ESP(Spell):
    name = "ESP"
    class_level_map = {
        classes.MagicUser: 2,
    }
    duration = SpellDuration(duration_per_level=units.GameTurn(1))
    range = SpellRange(base_range=units.Feet(60))
