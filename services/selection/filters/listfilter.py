from clubsandwich.ui import UIScene, LabelView

from services.selection.filters.base import SelectionFilter
from ui.views import KeyAssignedListView


class ListBasedSelectionFilter(SelectionFilter):
    """
    A Selection Filter using the type inheritance to filter.
    """

    def __init__(self):
        super().__init__()
        self.view = None

    def filter(self, targets):
        self.view = ListFilterView(targets)
        self.view.director.push_scene(self.view)


class ListFilterView(UIScene):
    covers_screen = False

    def __init__(self, targets):
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
