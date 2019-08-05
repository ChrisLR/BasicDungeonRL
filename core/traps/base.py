import abc


class Trap(object):
    __metaclass__ = abc.ABCMeta
    base_trap = None

    @classmethod
    @abc.abstractmethod
    def trigger(cls, host, event):
        pass
