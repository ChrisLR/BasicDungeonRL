from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Instantaneous
from bflib.spells.range import SpellRange


@listing.register_spell
class Fireball(Spell):
    name = "Fireball"
    class_level_map = {
        classes.MagicUser: 3,
    }
    duration = Instantaneous()
    range = SpellRange(
        base_range=units.Feet(100),
        range_per_level=units.Feet(10)
    )
