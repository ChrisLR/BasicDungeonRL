import abc


class Action(object):
    __metaclass__ = abc.ABCMeta

    must_recall = False
    recall_delay = None

    #: Iterable of the selection classes required to execute this action
    target_selection_types = None

    #: Filters to apply on the targets previously acquired
    target_filters = None

    def can_execute(self, character, selection=None):
        return True

    @abc.abstractclassmethod
    def execute(self, character, selection=None):
        pass

    def recall_execute(self, character, selection=None):
        pass


