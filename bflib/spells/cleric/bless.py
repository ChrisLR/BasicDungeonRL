from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRadius


@listing.register_spell
class Bless(Spell):
    name = "Bless"
    class_level_map = {
        classes.Cleric: 2,
    }
    duration = SpellDuration(duration_per_level=units.Minute(1))
    range = SpellRadius(base_radius=units.Feet(50))
    reverse_spell = Bane


@listing.register_spell
class Bane(Spell):
    name = "Bane"
    class_level_map = {
        classes.Cleric: 2,
    }
    duration = SpellDuration(duration_per_level=units.Minute(1))
    range = SpellRadius(base_range=units.Feet(50))
    reverse_spell = Bless
