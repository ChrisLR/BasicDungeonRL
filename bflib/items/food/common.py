from bflib.items.food.base import Food
from bflib.items import coins
from bflib import units
from bflib.sizes import Size


class DryRations(Food):
    name = "Dry Rations (One Week)"

    price = coins.Gold(10)
    size = Size.Medium
    wear_locations = tuple()
    weight = units.Pound(14)
