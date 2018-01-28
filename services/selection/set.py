class SelectionSet(object):
    """
    The purpose of this class is to allow
    an action to query multiple selections.
    """
    def __init__(self, selections, filters):
        self.selections = selections
        self.filters = filters
