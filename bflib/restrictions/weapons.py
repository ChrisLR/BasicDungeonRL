from bflib.keywords.weapons import WeaponWieldKeyword
from bflib.restrictions.base import Restriction
from bflib.sizes import Size


class WeaponRestrictionSet(Restriction):
    __slots__ = ["included", "excluded"]

    def __init__(self, included=None, excluded=None):
        self.included = included
        self.excluded = excluded

    def can_wield(self, item):
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
        )


class WeaponSizeRestrictionSet(Restriction):
    __slots__ = ["large", "medium", "small"]
    keywords = WeaponWieldKeyword

    _priority_map = {
        keywords.CanWield: 0,
        keywords.NeedsTwoHands: 1,
        keywords.CannotWield: 2
    }

    def __init__(self, large=keywords.CanWield, medium=keywords.CanWield, small=keywords.CanWield):
        self.large = large
        self.medium = medium
        self.small = small
        self.mapping = {
            Size.Small: self.small,
            Size.Medium: self.medium,
            Size.Large: self.large
        }

    def can_wield(self, item):
        keyword = self.mapping.get(item.size, self.keywords.CannotWield)
        if keyword == self.keywords.CannotWield:
            return False
        else:
            return keyword

    @classmethod
    def from_merge(cls, first, other):
        small = min(
            cls._priority_map[cls.keywords.CanWield],
            cls._priority_map[first.small],
            cls._priority_map[other.small]
        )

        medium = min(
            cls._priority_map[cls.keywords.CanWield],
            cls._priority_map[first.medium],
            cls._priority_map[other.medium]
        )

        large = min(
            cls._priority_map[cls.keywords.CanWield],
            cls._priority_map[first.large],
            cls._priority_map[other.large]
        )

        return cls(small=small, medium=medium, large=large)

