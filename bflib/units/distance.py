import abc

from bflib.units.base import Unit


class DistanceUnit(Unit):
    __metaclass__ = abc.ABCMeta


class Feet(DistanceUnit):
    pass
