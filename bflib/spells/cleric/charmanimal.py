from bflib import dice, units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import SpellDuration
from bflib.spells.range import SpellRange


@listing.register_spell
class CharmAnimal(Spell):
    name = "Charm Animal"
    class_level_map = {
        classes.Cleric: 2,
    }
    duration = SpellDuration(
        base_duration=dice.D4(1),
        duration_per_level=units.CombatRound(1)
    )
    range = SpellRange(base_range=units.Feet(60))
