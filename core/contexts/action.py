class Action(object):
    def __init__(self, actor, target):
        self.actor = actor
        self.target = target


class TwoTargetAction(object):
    def __init__(self, actor, target_one, target_two):
        self.actor = actor
        self.target_one = target_one
        self.target_two = target_two


class MultipleTargetAction(object):
    def __init__(self, actor, targets):
        self.actor = actor
        self.targets = targets
