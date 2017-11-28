from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class FloatingDisc(Spell):
    name = "Floating Disc"
    class_level_map = {
        classes.MagicUser: 1,
    }
    duration = SpellDuration(
        base_duration=units.GameTurn(5),
        duration_per_level=units.GameTurn(1)
    )
    range = SpellRange(units.Feet(0))
