from core.components.base import Component


class Sellable(Component):
    NAME = "sellable"

    def __init__(self, base_price):
        super().__init__()
        self.base_price = base_price

    @property
    def price(self):
        return self.base_price

    def copy(self):
        return Sellable(self.base_price)
