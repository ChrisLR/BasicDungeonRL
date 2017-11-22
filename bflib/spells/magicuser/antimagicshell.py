from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRadius


@listing.register_spell
class AntiMagicShell(Spell):
    name = "Anti-Magic Shell"
    class_level_map = {
        classes.MagicUser: 6,
    }
    duration = SpellDuration(duration_per_level=units.CombatRound(1))
    range = SpellRadius(base_radius=units.Feet(10))
