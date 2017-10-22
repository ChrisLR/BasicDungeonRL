from bflib import dice
from bflib import units
from bflib.items import coins
from bflib.items.base import Item


class Ammunition(Item):
    ammunition_type = None
    ammunition_damage = dice.Dice
    price = coins.Copper
    weight = units.Pound
