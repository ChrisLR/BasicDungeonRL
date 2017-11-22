from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.range import SpellRange


@listing.register_spell
class CharmPerson(Spell):
    name = "Charm Person"
    class_level_map = {
        classes.MagicUser: 1,
    }
    duration = None
    range = SpellRange(base_range=units.Feet(30))
