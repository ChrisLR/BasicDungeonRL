from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import Self


@listing.register_spell
class Commune(Spell):
    name = "Commune"
    class_level_map = {
        classes.Cleric: 5,
    }
    duration = SpellDuration(duration_per_level=units.CombatRound(1))
    range = Self()
