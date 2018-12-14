from bfgame.queries import listing
from bfgame.queries.base import CumulativeQuery


@listing.register_query
class Experience(CumulativeQuery):
    """
    This Query will allow registered components to return their experience worth.
    """
    name = "experience_value"

    @property
    def result(self):
        return sum(self._result)
