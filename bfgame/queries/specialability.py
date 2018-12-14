from collections import Iterable
from inspect import isclass

from bfgame.queries import listing
from bfgame.queries.base import CumulativeQuery


@listing.register_query
class SpecialAbility(CumulativeQuery):
    """
    This Query will allow registered components to return their special abilities.
    """
    name = "special_ability"

    def __init__(self, querier):
        super().__init__(querier)
        self._result = {}

    def do_query(self, abilities=None):
        """
        :param abilities: An Optional filter to specify which type to retrieve
        """
        if abilities is not None:
            if not isinstance(abilities, Iterable):
                abilities = [abilities]
        self.abilities = abilities
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
        if self.abilities:
            if isclass(value):
                if value not in self.abilities:
                    return False
            else:
                if not any([isinstance(value, ability_type) for ability_type in self.abilities]):
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
        amount_of_filters = len(self.abilities)
        if amount_of_filters == 1:
            return sum(self._result.values())

        if not amount_of_filters:
            return self._result

