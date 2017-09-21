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

    def evaluate(self, ability_score_set):
        stats = ("strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma")
        for stat in stats:
            if not self._eval_if_set(stat, ability_score_set):
                return False
        return True

    def _eval_if_set(self, stat, evaluated_set):
        current = getattr(evaluated_set, stat)
        minimum = getattr(self.minimum_set, stat, None)
        maximum = getattr(self.maximum_set, stat, None)

        if minimum is not None and current.value < minimum.value:
            return False

        if maximum is not None and current.value > maximum.value:
            return False

        return True

