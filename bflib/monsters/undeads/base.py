from bflib.monsters import listing
from bflib.monsters.base import Monster


@listing.register_type
class Undead(Monster):
    pass
