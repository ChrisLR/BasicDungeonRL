from services.echo import EchoService


class Facade(object):
    def __init__(self, game):
        self.echo = EchoService(game)
        self.game = game
