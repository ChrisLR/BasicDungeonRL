from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Permanent
from bflib.spells.range import SpellRange


@listing.register_spell
class Feeblemind(Spell):
    name = "Feeblemind"
    class_level_map = {
        classes.MagicUser: 5,
    }
    duration = Permanent()
    range = SpellRange(base_range=units.Feet(180))
