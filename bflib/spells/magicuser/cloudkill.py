from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class CloudKill(Spell):
    name = "Cloudkill"
    class_level_map = {
        classes.MagicUser: 5,
    }
    duration = SpellDuration(duration_per_level=units.CombatRound(6))
    range = SpellRange(
        base_range=units.Feet(100),
        range_per_level=units.Feet(10)
    )
