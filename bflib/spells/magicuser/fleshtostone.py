from bflib import units
from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Permanent
from bflib.spells.range import SpellRange


@listing.register_spell
class FleshToStone(Spell):
    name = "Flesh to Stone"
    class_level_map = {
        classes.MagicUser: 6,
    }
    duration = Permanent()
    range = SpellRange(range_per_level=units.Feet(30))
    reverse_spell = StoneToFlesh


@listing.register_spell
class StoneToFlesh(Spell):
    name = "Stone To Flesh"
    class_level_map = {
        classes.MagicUser: 6,
    }
    duration = Permanent()
    range = SpellRange(range_per_level=units.Feet(30))
    reverse_spell = FleshToStone
