from services.selection.filters.base import SelectionFilter


class TypeBasedFilter(SelectionFilter):
    """
    A Selection Filter using the type inheritance to filter.
    """
    __slots__ = ["type_filter"]

    def __init__(self, type_filter):
        self.type_filter = type_filter

    def filter(self, targets):
        return [target for target in targets
                if isinstance(target, self.type_filter)
                or issubclass(target, self.type_filter)]
