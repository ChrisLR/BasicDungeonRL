class Ability(object):
    name = ""
    # Either a TargetSelectionSet or a TargetSelectionChain
    target_selection = None

    def __init__(self, base_ability):
        self.base_ability = base_ability
