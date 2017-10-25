from bflib import units
from bflib.items import coins
from bflib.items.weapons.throwing.base import ThrowingWeapon


class OilFlask(ThrowingWeapon):
    name = "Oil Flask"

    price = coins.Gold(1)
    weight = units.Pound(1)
