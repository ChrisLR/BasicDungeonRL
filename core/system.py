class System(object):
    __slots__ = ["factory", "game", "ui", "services"]

    def __init__(self, game, factory, ui, services):
        self.factory = factory
        self.game = game
        self.ui = ui
        self.services = services
