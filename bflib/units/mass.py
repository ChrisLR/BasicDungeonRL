import abc
import numbers
from bflib.units.base import Unit


class MassUnit(Unit):
    __metaclass__ = abc.ABCMeta


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
