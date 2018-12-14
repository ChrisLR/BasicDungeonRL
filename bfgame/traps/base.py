import abc


class Trap(object):
    __metaclass__ = abc.ABCMeta
    base_trap = None

    @abc.abstractclassmethod
    def trigger(self, host, event):
        pass
