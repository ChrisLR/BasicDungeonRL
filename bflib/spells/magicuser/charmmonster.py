from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Special
from bflib.spells.range import SpellRange


@listing.register_spell
class CharmMonster(Spell):
    name = "Charm Monster"
    class_level_map = {
        classes.MagicUser: 4,
    }
    duration = Special()
    range = SpellRange(base_range=units.Feet(30))
