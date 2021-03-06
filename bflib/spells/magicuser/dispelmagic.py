from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Instantaneous
from bflib.spells.range import SpellRange


@listing.register_spell
class DispelMagic(Spell):
    name = "Dispel Magic"
    class_level_map = {
        classes.MagicUser: 3,
        classes.Cleric: 4,
    }
    duration = Instantaneous()
    range = SpellRange(units.Feet(120))
