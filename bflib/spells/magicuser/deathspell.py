from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Instantaneous
from bflib.spells.range import SpellRange


@listing.register_spell
class DeathSpell(Spell):
    name = "Death Spell"
    class_level_map = {
        classes.MagicUser: 6,
    }
    duration = Instantaneous
    range = SpellRange(units.Feet(240))
