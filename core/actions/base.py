import abc


class Action(object):
    __metaclass__ = abc.ABCMeta
    id = None

    must_recall = False
    recall_delay = None

    # Either a TargetSelectionSet or a TargetSelectionChain
    target_selection = None

    def can_execute(self, character, target_selection=None):
        return True

    @abc.abstractclassmethod
    def execute(self, character, target_selection=None):
        pass

    def recall_execute(self, character, selection=None):
        pass


