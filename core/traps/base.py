import abc


class Trap(object):
    __metaclass__ = abc.ABCMeta
    base_trap = None

    @property
    def name(self):
        return self.base_trap.name

    @abc.abstractclassmethod
    def trigger(self, host, event):
        pass
