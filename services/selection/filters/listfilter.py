import functools

from bearlibterminal import terminal
from clubsandwich.ui import ButtonView, UIScene, WindowView, LayoutOptions

from core.game.manager import game
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
        game.game_context.director.push_scene(self.view)


class ListFilterView(UIScene):
    covers_screen = False

    def __init__(self, host_filter, targets):
        self.targets = targets
        controls = [
            SelectableButtonView(
                target.name,
                functools.partial(self.select_object, value=target)
            )
            for target in targets
        ]
        super().__init__([
            WindowView(
                "Select the items to get",
                subviews=[
                    KeyAssignedListView(controls, 64),
                    ButtonView("Finish", self.finish, layout_options=LayoutOptions.row_bottom(0.2)),
                ],
                layout_options=LayoutOptions(width=0.5, left=0.3, height=0.9, right=None, bottom=None),
            )


        ])
        self.host_filter = host_filter
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
        super().terminal_read(val)
        if val == terminal.TK_ESCAPE:
            self.host_filter.canceled = True
            self.director.pop_scene()
