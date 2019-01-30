from core.components import Component, listing


@listing.register
class Restrictions(Component):
    NAME = 'restrictions'
    __slots__ = ["restrictions"]

    def __init__(self):
        super().__init__()
        self.restrictions = None

    def on_register(self, host):
        super().on_register(host)
        self.restrictions = host.query.restrictions()

    @property
    def ability_score(self):
        return self.restrictions.ability_score

    @property
    def armor(self):
        return self.restrictions.armor

    @property
    def classes(self):
        return self.restrictions.classes

    @property
    def hit_dice_max_size(self):
        return self.restrictions.hit_dice_max_size

    @property
    def weapons(self):
        return self.restrictions.weapons

    @property
    def weapon_size(self):
        return self.restrictions.weapon_size

    def copy(self):
        return Restrictions()

    def __getattr__(self, item):
        if hasattr(self.restrictions, item):
            return getattr(self.restrictions, item)
        raise AttributeError()
