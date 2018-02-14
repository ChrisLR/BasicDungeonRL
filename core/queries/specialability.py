from collections import Iterable
from inspect import isclass

from core.queries import listing
from core.queries.base import CumulativeQuery


@listing.register_query
class SpecialAbility(CumulativeQuery):
    """
    This Query will allow registered components to return their special abilities.
    """
    name = "special_ability"

    def do_query(self, abilities=None):
        """
        :param abilities: An Optional filter to specify which type to retrieve
        """
        if abilities is not None:
            if not isinstance(abilities, Iterable):
                abilities = [abilities]
        self.abilities = abilities
        return super().do_query()

    def respond(self, value):
        if not self.abilities:
            self.result.append(value)
            return

        for ability_type in self.abilities:
            if isclass(value):
                if issubclass(value, ability_type):
                    self.result.append(value)
            else:
                if isinstance(value, ability_type):
                    self.result.append(value)

    def sum(self):
        return sum(int(element) for element in self.result)
