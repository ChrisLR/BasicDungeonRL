from bflib.restrictions.set import RestrictionSet
from bfgame.queries import listing
from bfgame.queries.base import CumulativeQuery


@listing.register_query
class Restrictions(CumulativeQuery):
    """
    This Query retrieves restrictions from all components
    """
    name = "restrictions"

    @property
    def result(self):
        restriction_set = RestrictionSet()
        for result in self._result:
            restriction_set = RestrictionSet.from_merge(restriction_set, result)

        return restriction_set
