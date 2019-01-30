from core.components import Component, listing


@listing.register
class Valuable(Component):
    NAME = "valuable"

    __slots__ = ["base_price"]

    def __init__(self, base_price):
        super().__init__()
        self.base_price = base_price

    @property
    def price(self):
        return self.base_price

    def copy(self):
        return Valuable(self.base_price)
