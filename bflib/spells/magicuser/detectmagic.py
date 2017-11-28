from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class DetectMagic(Spell):
    name = "Detect Magic"
    class_level_map = {
        classes.Cleric: 1,
        classes.MagicUser: 2,
    }
    duration = SpellDuration(base_duration=units.GameTurn(2))
    range = SpellRange(base_range=units.Feet(60))
