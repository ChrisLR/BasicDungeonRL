from core.components import listing, Component


@listing.register
class Gender(Component):
    NAME = "gender"
    __slots__ = ["gender"]

    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def copy(self):
        return Gender(self.value)
