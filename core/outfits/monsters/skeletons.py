from core.outfits.base import Outfit
from bflib import items


class SkeletonPack1(Outfit):
    name = "Skeleton Pack 1"
    worn_items = [
        items.ChainMail
    ]
    wielded_items = [
        items.Longsword,
        items.TowerShield
    ]
    inventory_items = [
    ]


class SkeletonPack2(Outfit):
    name = "Skeleton Pack 2"
    worn_items = [
        items.PlateMail
    ]
    wielded_items = [
        items.GreatAxe
    ]
    inventory_items = [
    ]
