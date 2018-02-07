import abc


class Effect(object):
    __metaclass__ = abc.ABCMeta
    name = ""

    @abc.abstractmethod
    def on_start(self, game_object):
        pass

    @abc.abstractmethod
    def update(self, game_object):
        pass

    @abc.abstractmethod
    def on_finish(self, game_object):
        pass


class Burning(Effect):
    name = "Burning"
    """
    Every round, deals Fire damage to the Host
    """
    def on_start(self, game_object):
        """
        Show a message, 
        :param game_object:
        :return:
        """

    def update(self, game_object):
        """
        At Each Update it deals damage to the game_object and shows a message
        :param game_object:
        :return:
        """
