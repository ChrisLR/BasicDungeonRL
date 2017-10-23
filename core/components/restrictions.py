from core.components import Component
from bflib.restrictions.set import RestrictionSet


class Restrictions(Component):
    NAME = 'restrictions'
    __slots__ = ["restrictions"]

    def __init__(self, *restriction_sets):
        super().__init__()
        self.restrictions = RestrictionSet()
        if restriction_sets:
            for restriction_set in restriction_sets:
                self.restrictions = RestrictionSet.from_merge(self.restrictions, restriction_set)

    def copy(self):
        return Restrictions(self.restrictions)

    def __getattr__(self, item):
        if hasattr(self.restrictions, item):
            return getattr(self.restrictions, item)
        raise AttributeError()
