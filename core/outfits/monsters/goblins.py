from core.outfits.base import Outfit
from bflib import items


class GoblinPack1(Outfit):
    name = "Goblin Pack 1"
    worn_items = [
        items.Cloak,
        items.LeatherArmor
    ]
    wielded_items = [
        items.Dagger
    ]
    inventory_items = [
    ]


class GoblinPack2(Outfit):
    name = "Goblin Pack 2"
    worn_items = [
        items.Cloak,
        items.LeatherArmor
    ]
    wielded_items = [
        items.Shortsword
    ]
    inventory_items = [
    ]
