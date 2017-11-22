from core.outfits.base import Outfit
from bflib import items


class Goblin(Outfit):
    name = "Goblin Pack 1"
    worn_items = [
        items.Cloak,
        items.LeatherArmor
    ]
    inventory_items = [
    ]
