from core.components.base import Component


class Money(Component):
    NAME = 'money'
    __slots__ = ["coins"]
    """
    This is the component that implements money
    """
    def __init__(self):
        super().__init__()
        self.coins = {}

    def copy(self):
        new = Money()
        new.coins = self.coins.copy()
        return new
