import abc


class Unit(object):
    __metaclass__ = abc.ABCMeta
    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value
