class System(object):
    __slots__ = ["factory", "game", "ui", "service"]

    def __init__(self, game=None, factory=None, ui=None, service=None):
        self.factory = factory
        self.game = game
        self.ui = ui
        self.service = service


class SystemObject(object):
    def __init__(self, system):
        self.system = system
