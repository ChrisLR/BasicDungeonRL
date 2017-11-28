from bflib.characters import classes
from bflib.spells import listing
from bflib.spells.base import Spell
from bflib.spells.duration import Instantaneous
from bflib.spells.range import Touch


@listing.register_spell
class CureSeriousWounds(Spell):
    name = "Cure Serious Wounds"
    class_level_map = {
        classes.Cleric: 4,
    }
    duration = Instantaneous()
    range = Touch()
    reverse_spell = CauseSeriousWounds


@listing.register_spell
class CauseSeriousWounds(Spell):
    name = "Cause Serious Wounds"
    class_level_map = {
        classes.Cleric: 4,
    }
    duration = Instantaneous()
    range = Touch()
    reverse_spell = CureSeriousWounds
