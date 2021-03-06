from core.components import listing, Component


@listing.register
class Consumable(Component):
    NAME = 'consumable'
    __slots__ = ["effects"]

    def __init__(self, *effects):
        super().__init__()
        self.effects = list(effects)

    def copy(self):
        return Consumable(self.effects.copy())
