class AllianceFacade(object):
    def __init__(self, game):
        self.game = game
        self.factions = {}

    def add_faction(self, faction):
        self.factions[faction.name] = faction

    def get_faction(self, name):
        return self.factions.get(name)
