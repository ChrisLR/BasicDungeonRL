from clubsandwich.ui import ButtonView, LabelView, UIScene

from services.selection.filters.base import SelectionFilter
from ui.views import KeyAssignedListView, SelectableButtonView


class ListBasedSelectionFilter(SelectionFilter):
    """
    A Selection Filter using the type inheritance to filter.
    """

    def __init__(self):
        super().__init__()
        self.view = None

    def filter(self, targets):
        self.view = ListFilterView(self, targets)
        self.view.director.push_scene(self.view)


class ListFilterView(UIScene):
    covers_screen = False

    def __init__(self, host_filter, targets):
        self.targets = targets
        controls = [SelectableButtonView(target.name, self.select_object) for target in targets]
        super().__init__([
            LabelView("Select the items to get"),
            KeyAssignedListView(controls),
            ButtonView("Finish", self.finish)
        ])
        self.host_filter = host_filter
        self.director.push_scene(self)
        self.selections = []

    def finish(self):
        self.host_filter.resolution = self.selections
        self.director.pop_scene()

    def select_object(self, value):
        if value in self.selections:
            self.selections.remove(value)
        else:
            self.selections.append(value)

    def terminal_read(self, val):
        action = actionmapping.lowercase_mapping.get(val, None)
        if not action:
            return

        if isinstance(action, Walk) or issubclass(action, Walk):
            self.director.pop_scene()
            self.selection_callback(action.direction)
