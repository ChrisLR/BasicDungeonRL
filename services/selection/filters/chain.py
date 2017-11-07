from services.selection.filters.base import SelectionFilter


class SelectionFilterChain(SelectionFilter):
    """
    A selection filter combining several to return one result.
    """
    __slots__ = ["filters"]

    def __init__(self, filters):
        self.filters = filters

    def filter(self, targets):
        filtered_targets = targets.copy()
        for selection_filter in self.filters:
            filtered_targets = selection_filter.filter(filtered_targets)

        return filtered_targets
