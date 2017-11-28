from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Special
from bflib.spells.range import SpellRange


@listing.register_spell
class Geas(Spell):
    name = "Geas"
    class_level_map = {
        classes.MagicUser: 6,
    }
    duration = Special()
    range = SpellRange(units.Feet(5))
    reverse_spell = ReverseGeas


@listing.register_spell
class ReverseGeas(Spell):
    name = "Reverse Geas"
    class_level_map = {
        classes.MagicUser: 6,
    }
    duration = Special()
    range = SpellRange(units.Feet(5))
    reverse_spell = Geas

