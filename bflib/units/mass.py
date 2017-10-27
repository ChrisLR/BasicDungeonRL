import abc
import numbers
import functools
from bflib.units.base import Unit


class MassUnit(Unit):
    __metaclass__ = abc.ABCMeta


@functools.total_ordering
class Pound(MassUnit):
    def __add__(self, other):
        if isinstance(other, Pound):
            return self.value + other.value
        if isinstance(other, numbers.Number):
            return self.value + other

        raise NotImplementedError()

    def __radd__(self, other):
        if isinstance(other, Pound):
            return self.value + other.value

        if isinstance(other, numbers.Number):
            return self.value + other

        raise NotImplementedError()

    def __eq__(self, other):
        if isinstance(other, Pound):
            return self.value.__eq__(other.value)

        if isinstance(other, numbers.Number):
            return self.value.__eq__(other)

        raise NotImplementedError()

    def __lt__(self, other):
        if isinstance(other, Pound):
            return self.value < other.value

        if isinstance(other, numbers.Number):
            return self.value < other

        raise NotImplementedError()

    def __gt__(self, other):
        if isinstance(other, Pound):
            return self.value > other.value

        if isinstance(other, numbers.Number):
            return self.value > other

        raise NotImplementedError()
