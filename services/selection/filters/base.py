import abc


class SelectionFilter(object):
    """
    Filters reduce the amount of targets acquired.
    They may use an UI the same way a Selection does.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, game_context, executor):
        self.game_context = game_context
        self.executor = executor
        self.canceled = False
        self.resolution = None
        self.view = None

    @abc.abstractmethod
    def filter(self, targets):
        pass
