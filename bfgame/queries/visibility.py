from bfgame.queries import listing
from bfgame.queries.base import CumulativeQuery


@listing.register_query
class Visibility(CumulativeQuery):
    name = "visibility"

    def __init__(self, querier):
        super().__init__(querier)
        self._result = set()

    def respond(self, value):
        self._result.add(value)

    @property
    def result(self):
        if not self._result:
            return True

        return list(self._result)
