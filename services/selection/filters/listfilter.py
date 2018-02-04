import functools
import collections

from bearlibterminal import terminal
from clubsandwich.ui import ButtonView, UIScene, WindowView, LayoutOptions

from core.game.manager import game
from services.selection.filters.base import SelectionFilter
from ui.views import KeyAssignedListView, SelectableButtonView


class ListFilterView(UIScene):
    covers_screen = False

    def __init__(self, host_filter, targets):
        self.targets = targets
        self.button_controls = collections.OrderedDict(
            (
                target,
                SelectableButtonView(
                    target.name,
                    functools.partial(self.select_object, value=target),
                    align_horz='left'
                )
            )
            for target in targets
        )
        super().__init__([
            WindowView(
                "",
                subviews=[
                    KeyAssignedListView(
                        self.button_controls.values(),
                        value_column_width=max(len(value.text) + 5 for value in self.button_controls.values()),
                        layout_options=LayoutOptions.column_left(0.9)),
                ],
                layout_options=LayoutOptions(width=0.5, left=0.3, height=0.9, right=None, bottom=None),
            ),
            ButtonView("Finish", self.finish, layout_options=LayoutOptions.row_bottom(0.2)),
        ])
        self.host_filter = host_filter
        self.selections = []

    def finish(self):
        self.host_filter.resolution = self.selections
        self.director.pop_scene()

    def select_object(self, value):
        if value in self.selections:
            self.button_controls[value].deselect()
            self.selections.remove(value)
        else:
            self.button_controls[value].select()
            self.selections.append(value)

    def terminal_read(self, val):
        super().terminal_read(val)
        if val == terminal.TK_ESCAPE:
            self.host_filter.canceled = True
            self.director.pop_scene()


class ListBased(SelectionFilter):
    """
    A Selection Filter using the type inheritance to filter.
    """
    view_class = ListFilterView

    def __init__(self, executor):
        super().__init__(executor)
        self.view = None

    def filter(self, targets):
        self.view = self.view_class(self, targets)
        game.game_context.director.push_scene(self.view)


class SingleListFilterView(ListFilterView):
    def select_object(self, value):
        self.selections = [value]
        self.finish()


class SingleListBased(ListBased):
    view_class = SingleListFilterView
