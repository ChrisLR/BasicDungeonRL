import abc

from bflib.units.base import Unit


class MassUnit(Unit):
    __metaclass__ = abc.ABCMeta


class Pound(MassUnit):
    pass
