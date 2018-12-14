from bfgame.effects.burning import Burning
from bfgame.effects.healing import Healing
from bfgame.effects.hidden import Hidden


listing = [Burning, Healing, Hidden]


def get_core_effect_from_base(base_effect):
    core_effect = next(
        (effect for effect in listing
         if effect.base_effect is base_effect)
    )

    return core_effect
