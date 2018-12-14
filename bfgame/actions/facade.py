from bfgame.actions import listing


class Facade(object):
    def __init__(self, game):
        self.game = game

    def get_action_by_name(self, name):
        action = listing.get_by_name(name)
        if action is not None:
            return action(self.game)
        return None
