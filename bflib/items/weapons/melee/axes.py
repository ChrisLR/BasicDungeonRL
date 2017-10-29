from bflib import dice
from bflib import units
from bflib.items import coins, listing
from bflib.items.weapons.melee.base import MeleeWeapon
from bflib.sizes import Size


@listing.register_type
class Axe(MeleeWeapon):
    pass


@listing.register_item
class HandAxe(Axe):
    name = "Hand Axe"

    melee_damage = dice.D4(1)
    price = coins.Gold(4)
    size = Size.Small
    weight = units.Pound(5)


@listing.register_item
class BattleAxe(Axe):
    name = "Battle Axe"

    melee_damage = dice.D8(1)
    price = coins.Gold(7)
    size = Size.Medium
    weight = units.Pound(7)


@listing.register_item
class GreatAxe(Axe):
    name = "Great Axe"

    melee_damage = dice.D10(1)
    price = coins.Gold(14)
    size = Size.Large
    weight = units.Pound(15)
