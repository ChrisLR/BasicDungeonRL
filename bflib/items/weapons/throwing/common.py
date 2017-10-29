from bflib import units
from bflib.items import coins, listing
from bflib.items.weapons.throwing.base import ThrowingWeapon


@listing.register_item
class OilFlask(ThrowingWeapon):
    name = "Oil Flask"

    price = coins.Gold(1)
    weight = units.Pound(1)
