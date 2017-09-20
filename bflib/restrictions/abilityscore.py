from bflib.restrictions.base import Restriction


class AbilityScoreRestrictionSet(Restriction):
    __slots__ = ["minimum_set", "maximum_set"]

    def __init__(self, minimum_set=None, maximum_set=None):
        self.minimum_set = minimum_set
        self.maximum_set = maximum_set

    @classmethod
    def from_merge(cls, first, other):
        return cls(
            minimum_set=type(first.minimum_set).from_merge(first.minimum_set, other.minimum_set),
            maximum_set=type(first.maximum_set).from_merge(first.maximum_set, other.maximum_set),
        )
