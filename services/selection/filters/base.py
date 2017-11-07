import abc


class SelectionFilter(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def filter(self, targets):
        pass
