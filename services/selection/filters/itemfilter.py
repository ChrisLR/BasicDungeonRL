import functools
import collections

from bearlibterminal import terminal
from clubsandwich.ui import ButtonView, UIScene, WindowView, LayoutOptions

from core import flags
from core.game.manager import game
from services.selection.filters.base import SelectionFilter
from ui.views import KeyAssignedListView, SelectableButtonView


class ItemFilter(SelectionFilter):
    """
    A Selection Filter that includes a hierarchy based on containers/contained
    """

    def __init__(self):
        super().__init__()
        self.view = None

    def filter(self, targets):
        items = [target for target in targets if flags.GameObjectFlags.Character in target.flags]
        self.view = ListFilterView(self, items)
        game.game_context.director.push_scene(self.view)


class ListFilterView(UIScene):
    covers_screen = False

    def __init__(self, host_filter, targets):
        self.targets = targets
        self.button_controls = collections.OrderedDict(
            (
                target,
                SelectableButtonView(
                    target.name,
                    functools.partial(self.select_object, value=target)
                )
            )
            for target in targets
        )
        super().__init__([
            WindowView(
                "",
                subviews=[
                    KeyAssignedListView(self.button_controls.values(), 64),
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
