from bflib.items.base import Item
from bflib.items import listing


@listing.register_type
class Coin(Item):
    __slots__ = ["amount"]
    value_in_copper = 0

    def __init__(self, amount):
        self.amount = amount

    def as_copper(self):
        return Copper(self.amount * self.value_in_copper)

    def as_silver(self):
        return Silver((self.amount * self.value_in_copper) / Silver.value_in_copper)

    def as_electrum(self):
        return Electrum((self.amount * self.value_in_copper) / Electrum.value_in_copper)

    def as_gold(self):
        return Gold((self.amount * self.value_in_copper) / Gold.value_in_copper)

    def as_platinum(self):
        return Platinum((self.amount * self.value_in_copper) / Platinum.value_in_copper)


@listing.register_item
class Copper(Coin):
    value_in_copper = 1


@listing.register_item
class Silver(Coin):
    value_in_copper = 10


@listing.register_item
class Electrum(Coin):
    value_in_copper = 50


@listing.register_item
class Gold(Coin):
    value_in_copper = 100


@listing.register_item
class Platinum(Coin):
    value_in_copper = 500
