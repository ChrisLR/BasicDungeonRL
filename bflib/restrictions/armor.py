from bflib.restrictions.base import Restriction
from bflib.items.shields.base import Shield


class ArmorRestrictionSet(Restriction):
    __slots__ = ["included", "excluded", "shields"]

    def __init__(self, included=None, excluded=None, shields=True):
        self.included = included
        self.excluded = excluded
        self.shields = shields

    @classmethod
    def from_merge(cls, first, other):
        included = []
        if first.included and other.included:
            included.extend(first.included)
            included.extend(other.included)
            included = list(set(included))

        excluded = []
        if not included:
            if first.excluded or other.excluded:
                excluded.extend(first.excluded)
                excluded.extend(other.excluded)

        return cls(
            included=included,
            excluded=excluded,
            shields=True if first.shields or other.shields else False
        )

    def can_wear(self, item):
        if not self.shields:
            if isinstance(item, Shield):
                return False

        if self.included is not None:
            for included_type in self.included:
                if isinstance(item, included_type):
                    return True
            return False

        if self.excluded is not None:
            for excluded_type in self.excluded:
                if isinstance(item, excluded_type):
                    return False

        return True
