import abc


class SelectionFilter(object):
    """
    Filters reduce the amount of targets acquired.
    They may use an UI the same way a Selection does.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, executor):
        self.executor = executor
        self.canceled = False
        self.resolution = None

    @abc.abstractmethod
    def filter(self, targets):
        pass
