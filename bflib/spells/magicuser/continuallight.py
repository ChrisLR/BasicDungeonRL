from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class ContinualLight(Spell):
    name = "Continual Light"
    class_level_map = {
        classes.Cleric: 3,
        classes.MagicUser: 2,
    }
    duration = SpellDuration(duration_per_level=units.Year(1))
    range = SpellRange(base_range=units.Feet(360))
    reverse_spell = ContinualDarkness


@listing.register_spell
class ContinualDarkness(Spell):
    name = "Continual Darkness"
    class_level_map = {
        classes.Cleric: 3,
        classes.MagicUser: 2,
    }
    duration = SpellDuration(duration_per_level=units.Year(1))
    range = SpellRange(base_range=units.Feet(360))
    reverse_spell = ContinualLight
