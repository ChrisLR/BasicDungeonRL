from bflib import items
from core.outfits import listing, Outfit


@listing.register
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


@listing.register
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
