from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class Confusion(Spell):
    name = "Confusion"
    class_level_map = {
        classes.MagicUser: 4,
    }
    duration = SpellDuration(
        base_duration=units.CombatRound(2),
        duration_per_level=units.CombatRound(1)
    )
    range = SpellRange(base_range=units.Feet(360))
