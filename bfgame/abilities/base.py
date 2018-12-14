class Ability(object):
    name = ""
    # Either a TargetSelectionSet or a TargetSelectionChain
    target_selection = None

    def __init__(self, game):
        self.game = game
