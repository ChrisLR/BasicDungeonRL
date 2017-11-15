from bflib.monsters.base import Monster
from bflib.monsters import listing


@listing.register_type
class Plant(Monster):
    pass
