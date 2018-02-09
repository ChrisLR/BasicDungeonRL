from bflib import dice, effects, units
from bflib.items import listing
from bflib.items.potions.base import Potion
from bflib.sizes import Size


@listing.register_item
class PotionOfHealing(Potion):
    name = "Potion of Healing"

    effect = effects.Healing(units.CombatRound(0), dice.D6(1, 1))
    price = None
    size = Size.Small
    weight = units.Pound(0.5)
