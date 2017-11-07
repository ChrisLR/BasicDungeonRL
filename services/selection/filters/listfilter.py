from services.selection.filters.base import SelectionFilter
from clubsandwich.ui import UIScene, LabelView, KeyAssignedListView


class ListBasedSelectionFilter(SelectionFilter):
    """
    A Selection Filter using the type inheritance to filter.
    """
    __slots__ = ["callback"]

    def __init__(self, callback):
        self.callback = callback

    def filter(self, targets):
        ListFilterView(targets, self.callback)


class ListFilterView(UIScene):
    covers_screen = False

    def __init__(self, targets, selection_callback):
        KeyAssignedListView()
        super().__init__([LabelView("Choose a direction.")])
        self.selection_callback = selection_callback
        self.director.push_scene(self)

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if not action:
            return

        if isinstance(action, Walk) or issubclass(action, Walk):
            self.director.pop_scene()
            self.selection_callback(action.direction)
