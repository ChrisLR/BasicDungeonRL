from bflib import units
from bflib.items import coins, listing
from bflib.items.magical.base import MagicItem
from bflib.items.weapons.melee.staves import Staff
from bflib.sizes import Size


@listing.register_type
class MagicStaff(Staff, MagicItem):
    name = "Staff"

    price = coins.Gold
    size = Size.Small
    weight = units.Pound(0)
