import abc


class Action(object):
    __metaclass__ = abc.ABCMeta

    must_recall = False
    recall_delay = None
    target_required = False
    target_selection_type = None
    target_type = None

    def can_execute(self, character, selection=None):
        return True

    @abc.abstractclassmethod
    def execute(self, character, selection=None):
        pass

    def recall_execute(self, character, selection=None):
        pass
