from bflib.restrictions.base import Restriction


class ClassRestrictionSet(Restriction):
    __slots__ = ["access_combined", "included", "excluded"]

    def __init__(self, included=None, excluded=None, access_combined=False):
        """
        :param included: Iterable, If Set, this restricts class selection to those defined.
        :param excluded: Iterable, If Set, this prevents defined classes to be selected.
        :param access_combined: Bool, If True, this allows the character to use combined classes.
        """
        self.included = included
        self.excluded = excluded
        self.access_combined = access_combined

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
            access_combined=True if first.shields or other.shields else False
        )

    def evaluate(self, character_class):
        if self.included and character_class not in self.included:
            return False

        if self.excluded and character_class in self.excluded:
            return False

        return True
