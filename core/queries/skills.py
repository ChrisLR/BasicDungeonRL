from collections import Iterable
from inspect import isclass

from core.queries import listing
from core.queries.base import CumulativeQuery


@listing.register_query
class Skills(CumulativeQuery):
    """
    This Query will allow registered components to return their special abilities.
    """
    name = "skills"

    def __init__(self, querier):
        super().__init__(querier)
        self._result = {}

    def do_query(self, skills=None):
        """
        :param skills: An Optional filter to specify which type to retrieve
        """
        if skills is not None:
            if not isinstance(skills, Iterable):
                skills = [skills]
        self.skills = skills
        return super().do_query()

    def respond(self, values):
        if isinstance(values, Iterable):
            for value in values:
                if self.valid_type(value):
                    self.add_cumulative(value)
        else:
            if self.valid_type(values):
                self.add_cumulative(values)

    def valid_type(self, value):
        if self.skills:
            if isclass(value):
                if value not in self.skills:
                    return False
            else:
                if not any([isinstance(value, skill_type) for skill_type in self.skills]):
                    return False

        return True

    def add_cumulative(self, value):
        if isclass(value) or not hasattr(value, 'value'):
            current = self._result.get(value)
            if not current:
                self._result[value] = 1
        else:
            current = self._result.get(value, 0)
            self._result[value] = current + value.value

    @property
    def result(self):
        amount_of_filters = len(self.skills)
        if amount_of_filters == 1:
            return sum(self._result.values())

        if not amount_of_filters:
            return self._result
