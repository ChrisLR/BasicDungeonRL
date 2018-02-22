from core.queries.base import CumulativeQuery


class Visibility(CumulativeQuery):
    name = "visibility"

    def __init__(self, querier):
        super().__init__(querier)
        self._result = {}

    def respond(self, value):
        """
        The Value Dict contains the Type of Visibility and Bool Result for visible
        :param value: Dictionary containing Type and Bool
        :type value: dict
        """
        