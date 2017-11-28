from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class FindTraps(Spell):
    name = "Find Traps"
    class_level_map = {
        classes.Cleric: 2,
    }
    duration = SpellDuration(base_duration=units.GameTurn(3))
    range = SpellRange(units.Feet(30))
